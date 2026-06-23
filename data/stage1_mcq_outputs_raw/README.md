# Stage 1 — raw MCQ outputs

36 CSV files corresponding to model x RAG condition x temperature combinations:
- 12 models x 2 RAG conditions at T = 0 (24 files)
- 6 efficient-tier models x 2 RAG conditions at T = 0.7 (12 files)

Each file contains N = 3 repeated MCQ responses (150 rows = 50 questions x 3 runs) with fields:

`question_id`, `model_family`, `model_version`, `rag_condition`, `temperature`, `run_number`, `raw_output`, `parsed_answer`, `correct_answer`, `is_correct`.

The 50 MCQ questions and answer key are provided in the Supplementary Information accompanying the manuscript. Aggregate accuracy per cell is summarised in `results/stage1_mcq_summary/stage1_accuracy_summary_T0_T07.md`.
