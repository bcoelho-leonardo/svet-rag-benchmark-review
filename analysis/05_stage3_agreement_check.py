"""Stage 3 human evaluation: reviewer tallies (Table 4), Fleiss' kappa (Part 1) and pairwise Cohen's kappa.
Run from the package root:  python analysis/05_stage3_agreement_check.py
Reads stage3_human_evaluation/evaluators_responses_anonymised.txt (reviewers identified by role only).
Fleiss' kappa is implemented directly (no statsmodels dependency). Bootstrap intervals (Table S16) are in the
October notebook (notebooks/Revision_analyses_October2026.ipynb).
"""
import os, sys, csv
from itertools import combinations
from pathlib import Path
import numpy as np, pandas as pd
from sklearn.metrics import cohen_kappa_score
ROOT = Path(__file__).resolve().parents[1]; os.chdir(ROOT)
rows = [r[:12] for r in csv.reader(open("stage3_human_evaluation/evaluators_responses_anonymised.txt", encoding="utf-8", newline ="")) if r and r[0] != "reviewer"]
df = pd.DataFrame(rows, columns="reviewer,part,q,subtype,plus,minus,ex,ey,clarity,fact,conf,t".split(","))
def rag(c, p): return "Tie" if c == "Tie" else ("RAG+" if c == p else "RAG-")
for d in ("fact", "clarity"): df[d + "_r"] = [rag(c, p) for c, p in zip(df[d], df.plus)]
print("Table 4 – RAG+ share of non-tie judgments (correctness | clarity)")
for r, g in df.groupby("reviewer", sort=False):
    f = [(g[d + "_r"] == "RAG+").sum() for d in ("fact", "clarity")]; n = [(g[d + "_r"] != "Tie").sum() for d in ("fact", "clarity")]
    print(f"  {r:45s} N={len(g):2d}  {f[0]}/{n[0]} | {f[1]}/{n[1]}")
def fleiss(M):
    n = M.sum(1)[0]; N = M.shape[0]; p = M.sum(0) / (N * n); P = ((M ** 2).sum(1) - n) / (n * (n - 1))
    return (P.mean() - (p ** 2).sum()) / (1 - (p ** 2).sum())
ext1 = ["SVET Specialist I", "Local electrochemical techniques specialist", "Non-expert baseline"]
cats = ["RAG+", "RAG-", "Tie"]
print("\nFleiss' kappa, Part 1 (three external reviewers)")
for d, name in (("fact_r", "factual correctness"), ("clarity_r", "scientific clarity")):
    piv = df[(df.part == "1") & df.reviewer.isin(ext1)].pivot(index="q", columns="reviewer", values=d)
    M = np.array([[(piv.loc[i] == c).sum() for c in cats] for i in piv.index], float)
    print(f"  {name}: {fleiss(M):+.3f}")
print("\nPairwise Cohen's kappa (point estimates, external reviewers)")
for part, revs in (("1", ext1), ("2", ["SVET Specialist II", "Non-expert baseline"])):
    for a, b in combinations(revs, 2):
        out = []
        for d in ("fact_r", "clarity_r"):
            x = df[(df.reviewer == a) & (df.part == part)].set_index("q")[d].sort_index(); y = df[(df.reviewer == b) & (df.part == part)].set_index("q")[d].reindex(x.index)
            out.append(cohen_kappa_score(x, y))
        print(f"  Part {part}: {a} – {b}: correctness {out[0]:+.3f}, clarity {out[1]:+.3f}")
