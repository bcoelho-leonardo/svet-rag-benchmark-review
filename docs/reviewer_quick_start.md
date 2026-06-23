# Reviewer quick start

This repository is organised by evaluation stage. Each stage has a raw-output folder under `data/` and a summary folder under `results/`.

## To inspect Stage 1 (MCQ benchmark)

1. Open `data/stage1_mcq_outputs_raw/` to inspect the 36 raw CSV files, one per model x RAG condition x temperature combination.
2. Open `results/stage1_mcq_summary/stage1_accuracy_summary_T0_T07.md` for aggregate accuracy values (mean +/- SD across N = 3 runs).
3. The 50 MCQ questions and answer key are provided in the Supplementary Information accompanying the manuscript.

## To inspect Stage 2 (open-ended benchmark)

1. Open `data/stage2_open_ended_outputs_raw/`. Each CSV contains one model x RAG condition combination with 28 rows. RAG+ files include the `retrieved_context` field shown to the model per question.
2. Open `results/stage2_automated_metrics/stage2_bertscore_cosine_summary.md` for per-question BERTScore F1 and cosine similarity, aggregates, win/loss counts, and per-subtype means.
3. Open `data/stage2_llm_as_judge/results_perplexity_judge.csv` for the supplementary Perplexity Sonar pairwise evaluation discussed in the Supplementary Information.

## To inspect Stage 3 (blind human evaluation)

1. Open `data/stage3_human_evaluation/expert_part1_BLIND.csv` and `expert_part2_BLIND.csv` to view the blind evaluation forms shown to the five reviewers.
2. Open `expert_ground_truth_KEY.csv` to map the X/Y positional codes to RAG+ and RAG- responses.
3. Open `evaluators_responses_anonymised.csv` to inspect the anonymised evaluator judgments (SVET specialist I, SVET specialist II, local techniques specialist, non-expert, PI).

## To inspect code

Open the notebooks in `notebooks/` in numerical order:

- `01_stage1_mcq_benchmark.ipynb`
- `02_stage2_open_ended_benchmark.ipynb`
- `04_stage3_human_evaluation_analysis.ipynb`
- `05_stage3_figures.ipynb`

Numbering jumps from 02 to 04 because Stage 2 statistical analysis is folded into notebook 02 rather than placed in a separate notebook.

The notebooks were executed locally and may require path adjustments to rerun. Raw output files are included so that the reported analyses can be audited without rerunning paid LLM API calls.

## Prompts

The exact prompt templates used in the RAG- and RAG+ conditions of Stages 1, 2, and 3, plus the supplementary LLM-as-judge prompt, are provided under `prompts/`.
