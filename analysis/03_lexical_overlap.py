"""Lexical overlap between benchmark items and knowledge-base chunks.
Run from the package root:  python analysis/03_lexical_overlap.py
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
import sys,re,json,random,csv,collections,statistics as st
import bench_data as B
KB=need_full_kb()
MAN=MANIFEST
kb=json.load(open(KB,encoding='utf-8'))
man=list(csv.DictReader(open(MAN,encoding='utf-8')))
cls={m['kb_index_0based']:m for m in man}
def klass(i):
    a=man[i]['authorship_class']
    return 'PI' if a.startswith('pi_') else ('abstracts' if a=='third_party_published' else 'manufacturer')
STOP=set("a an the of to in on at by for with and or but is are was were be been being it its this that these those as from into than then so such can may might will would should could not no do does did has have had which who whom what why how when where if else over under above below between about via per also only both either each other more most less least any all some there their they them he she we you your our i one two".split())
def norm(t):
    t=t.lower().replace('−','-').replace('–','-').replace('µ','u').replace('×','x').replace('₂','2')
    return re.findall(r"[a-z0-9]+",t)
def content(toks): return {w for w in toks if w not in STOP and (len(w)>1 or w.isdigit())}
def grams(toks,n): return {tuple(toks[i:i+n]) for i in range(len(toks)-n+1)} if len(toks)>=n else set()
def longest_run(a,b):
    best=0; prev=[0]*(len(b)+1)
    for i in range(1,len(a)+1):
        cur=[0]*(len(b)+1)
        for j in range(1,len(b)+1):
            if a[i-1]==b[j-1]:
                cur[j]=prev[j-1]+1
                if cur[j]>best: best=cur[j]
        prev=cur
    return best
chunks=[]
for i,c in enumerate(kb):
    t=norm(c['text']); chunks.append((t,set(t),grams(t,3)))
def metrics(text):
    t=norm(text); cw=content(t); g3=grams(t,3)
    res=[]
    for i,(ct,cset,cg) in enumerate(chunks):
        c1=len(cw&cset)/len(cw) if cw else 0
        c3=len(g3&cg)/len(g3) if g3 else 0
        lr=longest_run(t,ct)
        res.append((c1,c3,lr))
    return t,res
def summarize(label,text):
    t,res=metrics(text)
    row={'n_tokens':len(t)}
    for name,idx in (('cont1',0),('cont3',1),('lcr',2)):
        vals=[r[idx] for r in res]; best=max(vals)
        bi=[i for i,v in enumerate(vals) if v==best]
        # tie-break: prefer by cont3 then lcr
        bi.sort(key=lambda i:(-res[i][1],-res[i][2],i)); i=bi[0]
        row[name]=round(best,3) if name!='lcr' else best
        row[name+'_chunk']=f'KB-{i+1:03d}'; row[name+'_source']=kb[i]['source']; row[name+'_class']=klass(i)
        row[name+'_pi_best']=max([res[j][idx] for j in range(len(kb)) if klass(j)=='PI'])
        row[name+'_third_best']=max([res[j][idx] for j in range(len(kb)) if klass(j)!='PI'])
    row['lcr_frac']=round(row['lcr']/len(t),3) if t else 0
    return row
items=[]
for q,qs,opts,k in B.MCQ:
    ans=opts['ABC'.index(k)]
    items.append(('S1',q,'question',qs)); items.append(('S1',q,'question+correct option',qs+' '+ans))
for q,sub,qs,ref in B.OPEN:
    items.append(('S2',q,'question',qs)); items.append(('S2',q,'reference (original)',ref))
    if q in B.AUDITED: items.append(('S2',q,'reference (audited)',B.AUDITED[q]))
rows=[]
for st_,q,kind,text in items:
    r=summarize(kind,text); r.update({'stage':st_,'qid':q,'unit':kind,'text':text}); rows.append(r)
cols=['stage','qid','unit','n_tokens','cont1','cont1_chunk','cont1_class','cont3','cont3_chunk','cont3_source','cont3_class','cont3_pi_best','cont3_third_best','lcr','lcr_frac','lcr_chunk','lcr_source','lcr_class','lcr_pi_best','lcr_third_best','cont1_pi_best','cont1_third_best','text']
with open('derived/lexical_overlap_per_item.csv','w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=cols,extrasaction='ignore'); w.writeheader(); w.writerows(rows)
# null: shuffled token order (keeps vocabulary, destroys phrases)
random.seed(20261108)
def null_stats(units,reps=10):
    c3=[];lr=[]
    for u in units:
        t=norm(u)
        for _ in range(reps):
            s=t[:]; random.shuffle(s)
            g3=grams(s,3); best3=max((len(g3&cg)/len(g3) if g3 else 0) for _,_,cg in chunks)
            bestl=max(longest_run(s,ct) for ct,_,_ in chunks)
            c3.append(best3); lr.append(bestl)
    return c3,lr
def q(v,p): v=sorted(v); return v[min(len(v)-1,int(p*(len(v)-1)+0.5))]
def desc(sel,key):
    v=[r[key] for r in sel]; return f"median {st.median(v):.3g}, IQR {q(v,.25):.3g}-{q(v,.75):.3g}, max {max(v):.3g}"
out=[]
groups=[('S1','question'),('S1','question+correct option'),('S2','question'),('S2','reference (original)')]
for s_,u in groups:
    sel=[r for r in rows if r['stage']==s_ and r['unit']==u]
    out.append(f"\n## {s_} | {u} | n={len(sel)}")
    out.append(f"  content-word containment (max over chunks): {desc(sel,'cont1')}")
    out.append(f"  word-trigram containment (max over chunks): {desc(sel,'cont3')}")
    out.append(f"  longest exact word run (words): {desc(sel,'lcr')} ; as fraction of item: {desc(sel,'lcr_frac')}")
    out.append(f"  items with trigram containment >=0.5: {sum(r['cont3']>=0.5 for r in sel)}; >=0.8: {sum(r['cont3']>=0.8 for r in sel)}; longest run >=8 words: {sum(r['lcr']>=8 for r in sel)}; >=15 words: {sum(r['lcr']>=15 for r in sel)}")
    cc=collections.Counter(r['cont3_class'] for r in sel); out.append(f"  class of best trigram match chunk: {dict(cc)}")
    sc=collections.Counter(r['cont3_source'] for r in sel); out.append(f"  source of best trigram match: {dict(sc.most_common())}")
    pi=sum(r['cont3_pi_best']>r['cont3_third_best'] for r in sel); th=sum(r['cont3_pi_best']<r['cont3_third_best'] for r in sel); tie=len(sel)-pi-th
    out.append(f"  best trigram match PI-class > third-party: {pi}; third-party > PI: {th}; equal: {tie}")
    c3,lr=null_stats([r['text'] for r in sel])
    out.append(f"  NULL (shuffled word order, 10 reps/item): trigram containment median {st.median(c3):.3g}, 95th pct {q(c3,.95):.3g}, max {max(c3):.3g}; longest run median {st.median(lr)}, 95th pct {q(lr,.95)}, max {max(lr)}")
# top items
def top(s_,u,key,n=8):
    sel=[r for r in rows if r['stage']==s_ and r['unit']==u]; sel.sort(key=lambda r:(-r[key],-r['cont3']))
    return sel[:n]
out.append("\n## Top Stage 2 references by longest exact run")
for r in top('S2','reference (original)','lcr'): out.append(f"  Q{r['qid']:02d} lcr={r['lcr']} ({r['lcr_frac']}) cont3={r['cont3']} {r['lcr_chunk']} {r['lcr_source'][:30]} [{r['lcr_class']}]")
out.append("\n## Top Stage 1 question+option by trigram containment")
for r in top('S1','question+correct option','cont3'): out.append(f"  Q{r['qid']:02d} cont3={r['cont3']} lcr={r['lcr']} {r['cont3_chunk']} {r['cont3_source'][:30]} [{r['cont3_class']}] | {r['text'][:70]}")
out.append("\n## Top Stage 2 references by trigram containment")
for r in top('S2','reference (original)','cont3'): out.append(f"  Q{r['qid']:02d} cont3={r['cont3']} lcr={r['lcr']} {r['cont3_chunk']} {r['cont3_source'][:30]} [{r['cont3_class']}]")
# audited vs original delta
out.append("\n## Audited vs original reference (6 clarified items): trigram containment / longest run")
for qn in B.AUDITED:
    o=[r for r in rows if r['stage']=='S2' and r['qid']==qn and r['unit']=='reference (original)'][0]; a=[r for r in rows if r['stage']=='S2' and r['qid']==qn and r['unit']=='reference (audited)'][0]
    out.append(f"  Q{qn:02d}: orig {o['cont3']}/{o['lcr']}  audited {a['cont3']}/{a['lcr']}")
open('derived/lexical_overlap_summary.txt','w').write('\n'.join(out)); print('\n'.join(out))
