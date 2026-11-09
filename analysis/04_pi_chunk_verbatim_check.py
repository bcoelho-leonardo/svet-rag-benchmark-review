"""Longest exact word run of each PI chunk against the third-party chunks.
Run from the package root:  python analysis/04_pi_chunk_verbatim_check.py
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
import json,csv,re,glob
KB=json.load(open(need_full_kb(),encoding='utf-8'))
man=list(csv.DictReader(open(MANIFEST,encoding='utf-8')))
tok=lambda s:re.findall(r"[a-z0-9]+(?:[-'][a-z0-9]+)*",s.lower())
T=[tok(c['text']) for c in KB]
cls=[m['authorship_class'] for m in man]
third=[i for i,c in enumerate(cls) if c.startswith('third_party')]
def lcs_run(a,b):
    # longest common contiguous word run via 8-gram index then extend
    best=0;pos=None
    idx={}
    for j in range(len(b)): idx.setdefault(b[j],[]).append(j)
    for i in range(len(a)):
        for j in idx.get(a[i],[]):
            if i>0 and j>0 and a[i-1]==b[j-1]: continue
            k=0
            while i+k<len(a) and j+k<len(b) and a[i+k]==b[j+k]: k+=1
            if k>best: best,pos=k,(i,j)
    return best,pos
rows=[]
for i,m in enumerate(man):
    if not m['authorship_class'].startswith('pi_'): continue
    b=(0,None,None)
    for t in third:
        k,p=lcs_run(T[i],T[t])
        if k>b[0]: b=(k,t,p)
    rows.append((m['chunk_id'],m['source_file'],m['authorship_class'],b[0],man[b[1]]['chunk_id'] if b[1] is not None else '',man[b[1]]['source_file'] if b[1] is not None else '', ' '.join(T[i][b[2][0]:b[2][0]+b[0]]) if b[1] is not None else ''))
import collections
for grp in ('pi_compiled_edited_ai_assisted','pi_curated_ai_assisted'):
    r=[x for x in rows if x[2]==grp]
    ks=sorted(x[3] for x in r)
    print(grp,len(r),'longest exact run vs any third-party chunk: median',ks[len(ks)//2],'max',ks[-1],' >=8:',sum(k>=8 for k in ks),' >=12:',sum(k>=12 for k in ks),' >=20:',sum(k>=20 for k in ks))
print()
for x in sorted(rows,key=lambda x:-x[3])[:10]:
    print(x[0],x[1][:22],x[2][:12],x[3],'vs',x[4],x[5][:20],'|',x[6][:150])
print('--- vs manufacturer chunks only')
manu=[i for i,c in enumerate(cls) if c=='third_party_manufacturer']
res=[]
for i,m in enumerate(man):
    if not m['authorship_class'].startswith('pi_'): continue
    k=max(lcs_run(T[i],T[t])[0] for t in manu)
    res.append((k,m['chunk_id'],m['source_file']))
res.sort(reverse=True);print(res[:5]);print('max',res[0][0],' >=8:',sum(r[0]>=8 for r in res))
