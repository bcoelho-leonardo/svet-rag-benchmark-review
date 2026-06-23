# Stage 3 — blind human expert evaluation

Five reviewers spanning a deliberate expertise gradient evaluated 21 paired RAG+ / RAG- responses (28 originally generated; 7 excluded due to model refusals in the RAG+ condition):

- SVET specialist I
- SVET specialist II
- Local techniques specialist
- Non-expert (baseline reviewer)
- PI (reported separately due to dual-role bias)

For each pair, responses were presented in randomised X/Y positions, blinded to RAG condition. Reviewers selected the more scientifically clear and the more factually correct response, free-text annotated specific errors, and rated their confidence.

## Files

- `expert_part1_BLIND.csv` — blind reviewer-facing Part 1 form (21 question pairs).
- `expert_part2_BLIND.csv` — blind reviewer-facing Part 2 form (21 question pairs).
- `expert_ground_truth_KEY.csv` — mapping of X/Y positional codes to RAG+ and RAG- responses for both parts.
- `evaluators_responses_anonymised.csv` — anonymised evaluator submissions from all five reviewers. Names removed.

Inter-rater agreement, preference, and confidence analyses are produced by `notebooks/04_stage3_human_evaluation_analysis.ipynb` and visualised in `notebooks/05_stage3_figures.ipynb`.
