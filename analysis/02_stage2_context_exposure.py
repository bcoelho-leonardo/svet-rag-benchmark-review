"""Stage 2 retrieved-context exposure by provenance class.
Run from the package root:  python analysis/02_stage2_context_exposure.py
Inputs are read with paths relative to the package root. Scripts that need the text of the
third-party knowledge-base chunks (withheld from the public release) read the full local file
given by the environment variable SVET_KB_FULL (the original embeddings_3072.json).
"""
import os, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
os.chdir(ROOT); sys.path.insert(0, str(ROOT / "analysis"))
KB_FULL = os.environ.get("SVET_KB_FULL")
MANIFEST = "kb/kb_provenance_manifest.csv"
def need_full_kb():
    if not KB_FULL or not Path(KB_FULL).exists():
        sys.exit("This script needs the full chunk text. Set SVET_KB_FULL to the original embeddings_3072.json "
                 "(third-party text is not part of the public release; see README).")
    return KB_FULL
import pandas as pd,json,csv,re,collections,numpy as np
KB=json.load(open(KB_FULL,encoding='utf-8')) if (KB_FULL and Path(KB_FULL).exists()) else None
man=list(csv.DictReader(open(MANIFEST,encoding='utf-8')))
idx={m['chunk_id']:i for i,m in enumerate(man)}
K=lambda i:('PI' if man[i]['authorship_class'].startswith('pi_') else ('abstracts' if man[i]['authorship_class']=='third_party_published' else 'manufacturer'))
import glob
recs=[]
for f in sorted(glob.glob('stage2_logs_sanitized/results_*RAG+_T0.0.csv')):
    df=pd.read_csv(f)
    for r in df.itertuples():
        ids=[idx[x] for x in str(r.retrieved_chunk_ids).split('|')] if isinstance(r.retrieved_chunk_ids,str) else []
        recs.append(dict(model=r.model,q=int(r.question_id[1:]),chunks=ids,resp=r.raw_response))
R=pd.DataFrame(recs)
print('RAG+ logs:',R.model.nunique(),'models; identical retrieved list across models for',int((R.groupby('q').chunks.apply(lambda s:len({tuple(x) for x in s}))==1).sum()),'/28 questions')
J=pd.read_csv('judge/reference_aware_judge_full28_sensitivity_v2_2026-10-06.csv')
print(J.shape, J.rag_condition.value_counts().to_dict())
Jp=J[J.rag_condition=='RAG+'].copy()
Jp['label']=Jp.judge_label.where(Jp.judge_label.notna(),'ABSTAIN')
print(Jp.label.value_counts(dropna=False).to_dict())
M=R.merge(Jp[['question_num','model','label','fully_correct']],left_on=['q','model'],right_on=['question_num','model'],how='left')
print('unmatched merges:',M.label.isna().sum())
# composition per response
for c in ['PI','manufacturer','abstracts']: M['n_'+c]=M.chunks.apply(lambda l:sum(K(i)==c for i in l))
M['top1']=M.chunks.apply(lambda l:K(l[0]))
M['top3_PI']=M.chunks.apply(lambda l:sum(K(i)=='PI' for i in l[:3]))
print('\nBase rate of PI chunks in KB: 56/146 = 38.4%; manufacturer 64 = 43.8%; abstracts 26 = 17.8%')
tot=M[['n_PI','n_manufacturer','n_abstracts']].sum(); print('Overall retrieved chunk composition (all 168 contexts x 10):',(tot/tot.sum()*100).round(1).to_dict())
Q=M.drop_duplicates('q')[['q','n_PI','n_manufacturer','n_abstracts','top1','top3_PI']]
print('Per-question (28 distinct contexts): mean PI chunks of 10 =',Q.n_PI.mean().round(2),'| questions with >=1 PI chunk:',int((Q.n_PI>0).sum()),'| top-1 class:',Q.top1.value_counts().to_dict(),'| PI chunks in top-3 mean',Q.top3_PI.mean().round(2))
print('\nBy judged outcome (RAG+ responses, n=168; contexts shared across models so clustered by question):')
g=M.groupby('label').agg(n=('q','size'),mean_PI_of10=('n_PI','mean'),mean_manuf=('n_manufacturer','mean'),mean_abs=('n_abstracts','mean'),pct_top1_PI=('top1',lambda s:(s=='PI').mean()*100),mean_top3_PI=('top3_PI','mean')).round(2)
print(g.to_string())
# any PI chunk
print('responses with zero PI chunks among 10:',(M.n_PI==0).sum(),'; of which CORRECT:',((M.n_PI==0)&(M.label=='CORRECT')).sum())
if KB is None:
    print('\n(best-supporting-chunk analysis skipped: needs SVET_KB_FULL)')
else:
    # support attribution: best-matching retrieved chunk for the response text
    def toks(t):
        t=t.lower().replace('−','-').replace('–','-').replace('µ','u'); return re.findall(r'[a-z0-9]+',t)
    def g3(t): return {tuple(t[i:i+3]) for i in range(len(t)-2)}
    rows=[]
    for r in M.itertuples():
        if r.label=='ABSTAIN': continue
        rt=toks(r.resp); rg=g3(rt)
        sc=[]
        for i in r.chunks:
            cg=g3(toks(KB[i]['text'])); sc.append(len(rg&cg)/len(rg) if rg else 0)
        best=max(sc); idx=[k for k,s in enumerate(sc) if s==best]
        classes={K(r.chunks[k]) for k in idx}
        rows.append(dict(label=r.label,q=r.q,model=r.model,best=best,cls=('PI' if classes=={'PI'} else ('third-party' if 'PI' not in classes else 'tie PI/third')),best_src=KB[r.chunks[idx[0]]]['source']))
    S=pd.DataFrame(rows)
    print('\nBest-supporting retrieved chunk for substantive RAG+ responses (response trigram containment; approximate):')
    print(S.groupby('label').best.agg(['count','median']).round(2).to_string())
    print(pd.crosstab(S.label,S.cls).to_string())
    print('CORRECT responses: best-support class PI / third / tie ->',(S[S.label=="CORRECT"].cls.value_counts()).to_dict())
    print('source files of best support (CORRECT):',S[S.label=='CORRECT'].best_src.value_counts().to_dict())
    print('\nweak support (best trigram containment <0.2) among CORRECT:',int(((S.label=="CORRECT")&(S.best<0.2)).sum()),'of',int((S.label=="CORRECT").sum()))

M.drop(columns=['chunks','resp']).to_csv('derived/stage2_retrieved_context_exposure.csv',index=False)
Q.to_csv('derived/stage2_retrieved_context_per_question.csv',index=False)
