# SVET RAG benchmark – reproducibility package (revision 2)

Companion material for *"Retrieval augmentation improves reliability of large language models for specialist
instrumentation: a three-stage evaluation using the scanning vibrating electrode technique"* (Digital Discovery).
Archive DOI: **[10.5281/zenodo.20820224](https://doi.org/10.5281/zenodo.20820224)** (version-specific) · Release tag: **v2.0-review**
(The tag names this research release only; the experiments themselves were not re-run.)

## 1. What is (and is not) in this package

| Folder | Content |
|---|---|
| `kb/` | `embeddings_3072_redacted.json` – 146 knowledge-base chunks, gemini-embedding-001 vectors (3072-d) for **all** chunks, chunk text for the **54** chunks written or compiled by the authors only; `kb_provenance_manifest.csv` – per-chunk source file, word span, provenance class, SHA-256 of the full chunk text, source URL and download information |
| `stage1_results/` | Raw logs of Stage 1: 50 MCQs × 12 models × RAG−/RAG+ at T = 0 (24 files, three runs each, `*_T0_*`) and the temperature-sensitivity runs at T = 0.7 for the six light models (12 files, `*_T07_*`); plus `stage1_provenance_sensitivity_summary.csv` |
| `stage2_logs_sanitized/` | Stage 2 logs for the six models; the retrieved-context text is replaced by `retrieved_chunk_ids` (ranked chunk IDs reconstructed by matching the logged context to the chunk texts; similarity scores were not logged) |
| `judge/` | Reference-aware judge (gpt-5.6-sol) prompt, manifest, validation, full results and sensitivity files; Perplexity judge results |
| `stage2_scores/` | `stage2_bertscore_cosine_per_question.csv` – per-question BERTScore F1 and cosine similarity, RAG+ vs RAG− (Table 3, Fig. 4). Scores are rounded to three decimals. Win/tie/loss labels (threshold ±0.01) were assigned from the unrounded values at scoring time, so a row whose rounded difference is exactly ±0.010 can be labelled either way (seven such rows); the pooled counts are 74 / 24 / 38 (RAG+ / RAG− / ties) over 136 pairs, as in the manuscript. Unrounded values were not saved for the original references |
| `stage3_human_evaluation/` | Blinded stimuli (`expert_part*_BLIND.csv`), the allocation key, and the reviewer responses (`evaluators_responses_anonymised.txt`; reviewers identified by role only, labels as in Table 4; submission timestamps removed, the `submitted_at` column is kept empty for compatibility with the notebooks) |
| `analysis/` | Diagnostic scripts used for the revision (see Section 3) |
| `derived/` | Outputs of those scripts |
| `notebooks/` | Executed notebooks (archival records; see Section 4) |
| `prompts/` | Stage 1 and Stage 2 prompt templates (RAG−/RAG+) and the Perplexity judge prompt |
| `results/` | Stage 1 accuracy summary (T = 0 and T = 0.7), recomputed from `stage1_results/` |
| `docs/` | Provenance/sensitivity-analysis freeze note (6 October 2026) and dates of generation, checksum of the freeze document (`freeze_document_checksum.md`) |

**Withheld.** The text of 90 chunks derived from third-party documents (Applicable Electronics system manual,
Science Wares ASET-LV4 user guide, bibliographic abstracts and reference lists of published work) is not
redistributed, and neither is the text of two author-compiled chunks that contain names/contact data of colleagues
(KB-015, KB-016). Their embeddings, source file, word span and SHA-256 are released. The remaining chunks contain
text written or compiled by the authors with the help of AI chat assistants (ChatGPT, Claude), reviewed and edited
by the PI; this is not independent validation, and the verbatim-overlap check against the third-party chunks is
described in SI Section S16.

Withholding third-party *source passages* is distinct from preserving the models' own response texts: the logs
and judge files keep every model output as generated, including short technical phrases (up to about 15 words)
that coincide with the manufacturer documents; these are part of the experimental record and are not redacted.

## 2. Reconstructing the withheld text (to re-run RAG+ conditions)

1. Download the two public documents (URLs in `kb/kb_provenance_manifest.csv`, columns `original_source_url`,
   `download_date`; the exact download date was not recorded and the documents carry no version or licence statement).
2. Convert to plain text and split each source file into 400-word windows with a 75-word overlap
   (`word_start_in_source`/`word_end_in_source` give the exact span of every chunk).
3. Compare the SHA-256 of each reconstructed chunk with `text_sha256`. The text-conversion step used in 2026 was not
   recorded, so hash mismatches caused by whitespace or extraction differences are possible; the released
   embeddings can then be used for retrieval with the withheld chunks replaced by your own reconstruction.

## 3. Diagnostic scripts (run from the package root)

```
python analysis/01_stage1_position_analysis.py       # Stage 1 answer-position / letter-prior diagnostics
python analysis/02_stage2_context_exposure.py        # retrieved-context composition by provenance class
export SVET_KB_FULL=/path/to/original/embeddings_3072.json   # full local KB (not released)
python analysis/03_lexical_overlap.py                # benchmark–KB lexical overlap (needs full text)
python analysis/04_pi_chunk_verbatim_check.py        # PI chunks vs third-party chunks (needs full text)
python analysis/05_stage3_agreement_check.py         # Stage 3: Table 4 tallies, Fleiss' kappa (Part 1), pairwise Cohen's kappa
python analysis/06_plot_fig5.py                      # Fig. 5 (reference-aware correctness, 28 questions); writes derived/figures/
```
Scripts 01 and 02 run on the released files; 03 and 04 need the full text and therefore only the outputs in `derived/`
are available to readers without it. `derived/figures/` holds the final Fig. 5 (PNG as used in the manuscript; PDF/SVG regenerated by script 06). All scripts are retrospective analyses of existing logs; none calls a model API.
`analysis/bench_data.py` holds the 50 MCQs and the 28 Stage 2 questions/references used by script 03.

## 4. Notebooks

The notebooks are archival records of the executed work, not turnkey pipelines: absolute local paths were replaced by
`<PROJECT_ROOT>`, API keys are read from a local `.env` that is not released (printed key prefixes were masked),
reviewer names were replaced by role labels, and outputs that printed third-party knowledge-base text were replaced by
a notice. Running the notebooks requires API keys for the respective providers and the full local KB.

## 5. Dates and environment

Stage 1: 3–4 March 2026 (one file, Llama-4-Scout RAG+ T = 0, has a 1 April 2026 modification time; see SI S12 and `docs/generation_date_range.md`).
Stage 2: 6 March 2026 (Sonar judge 7 March). Reference-aware judge and revision analyses: 6 October 2026.
Software versions: `requirements.txt` (Python 3.13.5 for the revision analyses; the March environment was not logged).

## 6. Licence

Code (`analysis/*.py`, `notebooks/`): MIT (`LICENSE`). Author-written text, documentation, metadata and derived data:
CC BY 4.0 (`LICENSE-DATA.md`, which also lists exceptions). Third-party material is not redistributed (Section 1).

## 7. Contact

Corresponding author: see the author list of the published article.

## 8. Integrity

`MANIFEST.sha256` lists the SHA-256 of every file in this package (`sha256sum -c MANIFEST.sha256`).
