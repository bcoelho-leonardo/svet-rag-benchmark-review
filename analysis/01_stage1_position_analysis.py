"""Stage 1 answer-position diagnostics (retrospective; no model calls).
Run from the package root:  python analysis/01_stage1_position_analysis.py
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
import pandas as pd,numpy as np
import glob
frames=[]
for f in sorted(glob.glob('stage1_results/results_*_T0_RAG*.csv')):
    d=pd.read_csv(f); d['model']=d['model_version'].str.replace('meta-llama/','',regex=False); d['cond']=d['rag_condition']; frames.append(d)
a=pd.concat(frames,ignore_index=True)
a['pred']=a.parsed_answer.astype(str).str.strip().str.upper().str[:1]
print('non-ABC parsed rows:',(~a.pred.isin(list('ABC'))).sum(), a[~a.pred.isin(list('ABC'))].groupby(['model','cond']).size().to_dict())
key=a.drop_duplicates('question_id').set_index('question_id').correct_answer
assert key.value_counts().to_dict()=={'B':37,'C':9,'A':4}
a['nonB']=a.correct_answer!='B'
order=['gpt-4o-mini','gpt-5.2','gemini-2.5-flash','gemini-2.5-pro','grok-4-1-fast','grok-4','deepseek-chat','deepseek-reasoner','Llama-4-Scout-17B-16E-Instruct','Llama-4-Maverick-17B-128E-Instruct','claude-haiku-4-5','claude-sonnet-4-6']
rng=np.random.default_rng(20261108)
rows=[]
for m in order:
    for c in ['RAG-','RAG+']:
        s=a[(a.model==m)&(a.cond==c)]
        r={'model':m,'cond':c}
        r['acc_all']=s.is_correct.mean()*100
        r['acc_Bkey(37)']=s[~s.nonB].is_correct.mean()*100
        r['acc_nonBkey(13)']=s[s.nonB].is_correct.mean()*100
        r['pred_B_%']=(s.pred=='B').mean()*100
        # letter-prior expectation: E[acc] if predictions independent of question, same letter marginals
        pk=key.value_counts(normalize=True)
        exp=[];pv=[]
        for run,g in s.groupby('run_number'):
            g=g.sort_values('question_id'); preds=g.pred.values; truth=g.correct_answer.values
            pl=pd.Series(preds).value_counts(normalize=True)
            exp.append(sum(pl.get(l,0)*pk.get(l,0) for l in 'ABC'))
            obs=(preds==truth).mean()
            perm=np.array([(rng.permutation(preds)==truth).mean() for _ in range(5000)])
            pv.append(((perm>=obs).sum()+1)/(len(perm)+1))
        r['letter_prior_exp_acc']=np.mean(exp)*100; r['perm_p_max_over_runs']=max(pv)
        # errors: share of wrong answers on nonB items that were 'B'
        w=s[(s.is_correct==0)]
        r['errors']=len(w); r['err_on_nonB_chose_B_%']=(w[w.nonB].pred=='B').mean()*100 if w.nonB.any() else np.nan
        r['err_on_nonB_n']=int(w.nonB.sum())
        rows.append(r)
R=pd.DataFrame(rows)
pd.set_option('display.width',250); pd.set_option('display.float_format',lambda x:f'{x:.1f}')
print(R.drop(columns=['perm_p_max_over_runs']).to_string(index=False))
print('\nmax permutation p over runs/models/conds:',R.perm_p_max_over_runs.max(), ' (5000 perms; min attainable 0.0002)')
print('\nmodel-conditions with acc below constant-B (74%):',R[R.acc_all<74][['model','cond','acc_all']].to_string(index=False))
# RAG effect by stratum, averaged over 12 models
P=R.pivot(index='model',columns='cond',values=['acc_all','acc_Bkey(37)','acc_nonBkey(13)'])
for k in ['acc_all','acc_Bkey(37)','acc_nonBkey(13)']:
    d=(P[(k,'RAG+')]-P[(k,'RAG-')]); print(f'{k}: mean RAG- {P[(k,"RAG-")].mean():.1f}  mean RAG+ {P[(k,"RAG+")].mean():.1f}  mean delta {d.mean():+.1f} pp; models improved {int((d>0).sum())}/12; declined {int((d<0).sum())}')
dn=(P[('acc_nonBkey(13)','RAG+')]-P[('acc_nonBkey(13)','RAG-')]); print('non-B delta by model:',dn.round(1).to_dict())
R.to_csv('derived/stage1_position_analysis.csv',index=False)
# letter distribution of predictions overall
print('\nPredicted letter share, all models pooled:'); print(a.groupby('cond').pred.value_counts(normalize=True).mul(100).round(1).unstack().to_string())
print('Key share: A 8, B 74, C 18')
