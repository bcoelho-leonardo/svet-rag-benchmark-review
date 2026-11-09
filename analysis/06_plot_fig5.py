"""Revised Fig. 5 (v7): larger print-friendly fonts, non-overlapping question labels.

Changes relative to v6:
- Question tick labels (Q01-Q28) are rotated 90 degrees with the * and † markers inline
  (e.g. "Q05†"). In v6 the horizontal bold labels were wider than their columns and ran
  together ("Q01Q02Q03...").
- Slightly taller figure and larger panel spacing to make room for the rotated labels.
- Everything else (data, colours, letters, brackets, legend, validation asserts) unchanged.

All font sizes are defined in the FONT block below.
"""
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm, ListedColormap
from matplotlib.patches import Patch

# --- File location ---------------------------------------------------------
# Package layout: input in judge/, outputs in derived/figures/ (paths relative to the package root).
BASE_DIR = (Path(__file__).resolve().parents[1] if "__file__" in globals() else Path.cwd())
CSV_FILE = BASE_DIR / "judge" / "reference_aware_judge_full28_sensitivity_v2_2026-10-06.csv"
OUTPUT_STEM = BASE_DIR / "derived" / "figures" / "Fig5_reference_aware_correctness_full28_v7"

# --- Font sizes (pt, at the native 16.2-inch figure width) ------------------
FONT = {
    "base": 18,
    "cell_letter": 20,   # C / P / I / A inside cells   (v5: 8.7)
    "ytick": 20,         # model names                  (v5: 13)
    "xtick": 16,         # Q01 ... Q28 (+ * and †), rotated (v5: 9.6)
    "subtype": 19,       # [A] ... [E] brackets         (v5: 12.5)
    "title": 23,         # RAG+ / RAG−                  (v5: 16)
    "xlabel": 18,        # Question ID                  (v5: 12.5)
    "legend": 18,        # legend                       (v5: 12)
}

# --- Read and validate data -----------------------------------------------
df = pd.read_csv(CSV_FILE)

MODEL_NAMES = {
    "gemini-2.5-flash": "Gemini 2.5 Flash",
    "gpt-4o-mini": "GPT-4o-mini",
    "grok-4-1-fast": "Grok-4-1-fast",
    "deepseek-chat": "DeepSeek-chat",
    "meta-llama/Llama-4-Scout-17B-16E-Instruct": "Llama-4-Scout",
    "claude-haiku-4-5": "Claude Haiku 4.5",
}
MODEL_ORDER = list(MODEL_NAMES)
Q_ORDER = list(range(1, 29))
RAG_ORDER = ["RAG+", "RAG-"]
EXCLUDED = {9, 11, 14, 17, 27, 28}
CONTEXT_AUDIT = {5, 15, 20}  # RAG+ only
LABELS = ["CORRECT", "PARTIAL", "INCORRECT", "ABSTAIN"]
LABEL_TO_NUM = {label: i for i, label in enumerate(LABELS)}

assert len(df) == 336, f"Expected 336 rows, got {len(df)}"
assert set(df["model"]) == set(MODEL_ORDER), "Unexpected/missing model identifiers"
assert set(df["question_num"]) == set(Q_ORDER), "Expected all Q01-Q28"
assert set(df["rag_condition"]) == set(RAG_ORDER), "Expected RAG+ and RAG-"
assert set(df["judge_label"]) <= set(LABELS), "Unexpected judge labels"
assert not df.duplicated(["model", "question_num", "rag_condition"]).any(), "Duplicate model-question-condition rows"
assert df["fully_correct"].eq(df["judge_label"].eq("CORRECT").astype(int)).all(), "Binary correctness mismatch"

question_meta = df.groupby("question_num").agg(
    subtype=("subtype", "first"),
    reference_basis=("reference_basis", "first"),
)
assert df.groupby("question_num")["subtype"].nunique().eq(1).all(), "Inconsistent question subtype"
assert df.groupby("question_num")["reference_basis"].nunique().eq(1).all(), "Inconsistent reference basis"
for q in Q_ORDER:
    expected_basis = "original_submitted_reference" if q in EXCLUDED else "provenance_audited_reference"
    assert question_meta.loc[q, "reference_basis"] == expected_basis, f"Unexpected reference basis for Q{q:02d}"

# --- Build matrices --------------------------------------------------------
matrices = {}
for condition in RAG_ORDER:
    subset = df.loc[df["rag_condition"] == condition]
    matrix = subset.pivot(index="model", columns="question_num", values="judge_label")
    matrix = matrix.reindex(index=MODEL_ORDER, columns=Q_ORDER)
    assert not matrix.isna().any().any(), f"Missing values in {condition}"
    matrices[condition] = matrix.apply(lambda col: col.map(LABEL_TO_NUM)).to_numpy(dtype=int)

# --- Plot -----------------------------------------------------------------
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": FONT["base"],
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "savefig.facecolor": "white",
})

status_colors = ["#3B936B", "#E3AD49", "#C65555", "#8E99A8"]
cmap = ListedColormap(status_colors)
norm = BoundaryNorm(np.arange(-0.5, 4.5, 1), cmap.N)
subtype_colors = {
    "A": "#264C82", "B": "#2776A8", "C": "#B47624",
    "D": "#38784D", "E": "#A03942",
}

fig, axes = plt.subplots(2, 1, figsize=(16.2, 11.4), facecolor="white")
fig.subplots_adjust(left=0.19, right=0.988, top=0.915, bottom=0.185, hspace=0.78)

letter_map = {"CORRECT": "C", "PARTIAL": "P", "INCORRECT": "I", "ABSTAIN": "A"}

for ax, condition in zip(axes, RAG_ORDER):
    ax.imshow(matrices[condition], cmap=cmap, norm=norm,
              interpolation="nearest", aspect="auto", origin="upper")
    ax.set_xlim(-0.5, 27.5)
    ax.set_ylim(5.5, -0.5)

    ax.set_yticks(np.arange(6), [MODEL_NAMES[m] for m in MODEL_ORDER])
    ax.tick_params(axis="y", length=0, pad=10, labelsize=FONT["ytick"])

    # Rotated labels with markers inline, e.g. "Q05†", "Q09*".
    tick_labels = [
        f"Q{q:02d}" + ("*" if q in EXCLUDED else "") + ("†" if condition == "RAG+" and q in CONTEXT_AUDIT else "")
        for q in Q_ORDER
    ]
    ax.set_xticks(np.arange(28), tick_labels)
    ax.tick_params(axis="x", length=0, pad=8, labelsize=FONT["xtick"], labelrotation=90)
    for tick, q in zip(ax.get_xticklabels(), Q_ORDER):
        tick.set_fontweight("bold")
        tick.set_color(subtype_colors[question_meta.loc[q, "subtype"]])
        tick.set_horizontalalignment("center")
        tick.set_verticalalignment("top")

    ax.set_xticks(np.arange(-0.5, 28, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, 6, 1), minor=True)
    ax.grid(which="minor", color="#FFFFFF", linewidth=1.2)
    ax.tick_params(which="minor", bottom=False, left=False)

    for ri in range(len(MODEL_ORDER)):
        for ci in range(len(Q_ORDER)):
            label = LABELS[matrices[condition][ri, ci]]
            txt_color = "#15212C" if label == "PARTIAL" else "white"
            ax.text(ci, ri, letter_map[label], ha="center", va="center",
                    fontsize=FONT["cell_letter"], fontweight="bold", color=txt_color)

    for spine in ax.spines.values():
        spine.set_visible(False)

    for subtype in "ABCDE":
        qs = [q for q in Q_ORDER if question_meta.loc[q, "subtype"] == subtype]
        start, end = min(qs) - 1, max(qs) - 1
        color = subtype_colors[subtype]
        ax.plot([start - 0.44, end + 0.44], [1.035, 1.035],
                transform=ax.get_xaxis_transform(), color=color, lw=2.8, clip_on=False)
        ax.text((start + end) / 2, 1.08, f"[{subtype}]",
                transform=ax.get_xaxis_transform(), ha="center", va="bottom",
                fontweight="bold", fontsize=FONT["subtype"], color=color, clip_on=False)

    ax.set_title("RAG+" if condition == "RAG+" else "RAG−",
                 fontsize=FONT["title"], fontweight="bold", pad=58)
    if condition == "RAG-":
        ax.set_xlabel("Question ID", fontsize=FONT["xlabel"], labelpad=12)

handles = [Patch(facecolor=c, edgecolor="none", label=f"{label[0]}  {label.title()}")
           for label, c in zip(LABELS, status_colors)]
fig.legend(handles=handles, loc="lower center", ncol=4,
           bbox_to_anchor=(0.59, 0.012), frameon=False, fontsize=FONT["legend"],
           handlelength=1.6, handleheight=1.2, columnspacing=2.2)

for ext in ("png", "pdf", "svg"):
    filename = OUTPUT_STEM.with_suffix(f".{ext}")
    fig.savefig(filename, dpi=500, bbox_inches="tight", facecolor="white")
    print("Saved:", filename)

print("\nPlotted classifications:")
print(pd.crosstab(df["rag_condition"], df["judge_label"]))
print("\nReference basis by question:")
print(question_meta["reference_basis"].value_counts())
plt.show()
