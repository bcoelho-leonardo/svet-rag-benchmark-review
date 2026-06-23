# File manifest

## Stage 1 — MCQ benchmark

### Raw outputs
Folder: `data/stage1_mcq_outputs_raw/`

36 CSV files corresponding to model x RAG condition x temperature combinations:
- 12 models x 2 RAG conditions at T = 0 (24 files)
- 6 efficient-tier models x 2 RAG conditions at T = 0.7 (12 files)

Each file contains N = 3 repeated MCQ responses with fields:
`question_id`, `model_family`, `model_version`, `rag_condition`, `temperature`, `run_number`, `raw_output`, `parsed_answer`, `correct_answer`, `is_correct`.

The Stage 1 question bank and answer key are provided in the Supplementary Information.

### Summary results
Folder: `results/stage1_mcq_summary/`

`stage1_accuracy_summary_T0_T07.md` — aggregate accuracy per model x RAG x temperature cell (mean +/- SD across N = 3 runs).

## Stage 2 — Open-ended benchmark

### Raw outputs
Folder: `data/stage2_open_ended_outputs_raw/`

12 CSV files corresponding to six efficient-tier models under RAG- and RAG+ conditions. RAG+ files include the retrieved context shown to the model per question.

Each file contains 28 rows with fields including:
`question_id`, `subtype`, `model`, `rag_condition`, `temperature`, `finish_reason`, `question_text`, `raw_response`, `retrieved_context` (RAG+ only), `n_chunks_retrieved` (RAG+ only), `ground_truth`.

Filename convention note: one Gemini RAG+ file uses `gemini-2_5-flash` rather than `gemini-2.5-flash`. This reflects the original code output and is preserved for traceability with the notebook.

### Automated metrics summary
Folder: `results/stage2_automated_metrics/`

`stage2_bertscore_cosine_summary.md` — per-question BERTScore F1 and cosine similarity, aggregates, win/loss counts, and per-subtype means for each of the six models.

### LLM-as-judge supplementary evaluation
Folder: `data/stage2_llm_as_judge/`

`results_perplexity_judge.csv` — output of the supplementary Perplexity Sonar pairwise judge experiment described in the Supplementary Information.

## Stage 3 — Human expert evaluation

Folder: `data/stage3_human_evaluation/`

- `expert_part1_BLIND.csv` — blind reviewer-facing Part 1 file (21 question pairs).
- `expert_part2_BLIND.csv` — blind reviewer-facing Part 2 file (21 question pairs).
- `expert_ground_truth_KEY.csv` — X/Y to RAG condition mapping for both parts.
- `evaluators_responses_anonymised.csv` — anonymised evaluator responses from all five reviewers (SVET specialist I, SVET specialist II, local techniques specialist, non-expert, PI). Names removed.

## Knowledge base

Folder: `data/knowledge_base/`

- `embeddings_3072.json` — 3,072-dimensional `gemini-embedding-001` vector store used by the RAG pipeline. The curated source documents are not included in this peer-review release.

## Prompts

Folder: `prompts/`

- `stage1/RAGminus_prompt.txt` — Stage 1 MCQ prompt, pretrained knowledge only.
- `stage1/RAGplus_prompt.txt` — Stage 1 MCQ prompt with retrieved context block.
- `stage2/RAGminus_prompt.txt` — Stage 2 and Stage 3 open-ended prompt, pretrained knowledge only.
- `stage2/RAGplus_prompt.txt` — Stage 2 and Stage 3 open-ended prompt with retrieved context block.
- `stage2/perplexity_judge_prompt.txt` — supplementary LLM-as-judge prompt.

## Notebooks

Folder: `notebooks/`

- `01_stage1_mcq_benchmark.ipynb` — Stage 1 benchmark execution and accuracy analysis.
- `02_stage2_open_ended_benchmark.ipynb` — Stage 2 benchmark execution, BERTScore F1 and cosine similarity scoring, statistical analysis.
- `04_stage3_human_evaluation_analysis.ipynb` — Stage 3 inter-rater agreement and preference analysis.
- `05_stage3_figures.ipynb` — figure generation for Stage 3 results.

Numbering jumps from 02 to 04 because Stage 2 statistical analysis is integrated into notebook 02 rather than placed in a separate notebook.
