# SVET RAG LLM Benchmark — Reviewer Access Repository

This repository contains the reviewer-access version of the code, data, prompts, model-output logs, and analysis files associated with the manuscript:

**Retrieval augmentation improves reliability of large language models for specialist instrumentation: a three-stage evaluation using the scanning vibrating electrode technique.**

## Archival DOI

A Zenodo record has been reserved for the frozen archival release of this work:

- **DOI:** [10.5281/zenodo.20820224](https://doi.org/10.5281/zenodo.20820224)

The DOI is reserved during peer review and will be activated upon acceptance, when a snapshot of this repository is deposited at Zenodo.

## Repository status

This repository is provided for peer review during the *Digital Discovery* submission process. It is not the final archival release. After acceptance, a cleaned and frozen public release will be deposited on Zenodo under the DOI above.

## Contents

- `notebooks/` — Jupyter notebooks for Stage 1, Stage 2, Stage 3, and figure generation.
- `prompts/` — prompt templates used for the RAG- and RAG+ conditions, and for the supplementary LLM-as-judge experiment.
- `data/knowledge_base/` — the 3,072-dimensional embedding store used by the RAG pipeline.
- `data/stage1_mcq_outputs_raw/` — raw Stage 1 multiple-choice model outputs (36 files: 12 models x 2 RAG conditions at T = 0, plus 6 efficient-tier models x 2 RAG conditions at T = 0.7).
- `data/stage2_open_ended_outputs_raw/` — raw Stage 2 open-ended model outputs (12 files: 6 efficient-tier models x 2 RAG conditions). RAG+ files include the retrieved context per question.
- `data/stage2_llm_as_judge/` — supplementary Perplexity Sonar pairwise evaluation file.
- `data/stage3_human_evaluation/` — blind reviewer-facing files, ground-truth key, and anonymised evaluator responses.
- `results/` — processed summary tables supporting the manuscript and Supplementary Information.
- `docs/` — repository notes, generation date range, and reviewer quick-start guide.

## Reproducibility note

Commercial LLM outputs are not exactly reproducible because provider-side models can be updated or deprecated at any time. This repository therefore provides the raw per-call input/output logs used in the study (model identifier, RAG condition, temperature, run number, raw output, parsed output, retrieved context where applicable, and scoring fields) so that the reported analyses can be audited without rerunning paid API calls.

## Question banks

The 50-question Stage 1 MCQ benchmark and the 28-question Stage 2 open-ended benchmark are provided in the Supplementary Information accompanying the manuscript. The Stage 2 output CSVs also include `question_text` and `ground_truth` columns for each evaluated item.

## Generation date range

All commercial LLM API calls analysed in this study were generated between 3 March 2026 and 7 March 2026 using each provider's official Python SDK.

## Knowledge base

For this peer-review release, only the embedding store (`data/knowledge_base/embeddings_3072.json`) is included. The full curated source documents that compose the SVET knowledge base are retained by the authors and will be addressed in the final archival release after peer review.

## Contact

For questions during peer review: Leonardo B. Coelho — leonardo@ialto.com.br

## License

This peer-review version is provided for manuscript evaluation. Final licensing for the public archival release will be specified upon acceptance. See `LICENSE`.
