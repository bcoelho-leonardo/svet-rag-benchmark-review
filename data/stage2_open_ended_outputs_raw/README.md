# Stage 2 — raw open-ended outputs

12 CSV files corresponding to six efficient-tier models (claude-haiku-4-5, gpt-4o-mini, gemini-2.5-flash, grok-4-1-fast, deepseek-chat, Llama-4-Scout-17B-16E-Instruct) under RAG- and RAG+ conditions, all at T = 0.

Each file contains 28 rows (one per open-ended question) with fields including:

`question_id`, `subtype`, `model`, `rag_condition`, `temperature`, `finish_reason`, `question_text`, `raw_response`, `retrieved_context` (RAG+ only), `n_chunks_retrieved` (RAG+ only), `ground_truth`.

Filename convention note: one Gemini RAG+ file uses `gemini-2_5-flash` rather than `gemini-2.5-flash`. This reflects the original code output and is preserved for traceability with the notebook.

The 28 open-ended questions, their subtypes, and ground truths are also provided in the Supplementary Information. Per-question BERTScore F1, cosine similarity, aggregates, and win/loss counts are summarised in `results/stage2_automated_metrics/stage2_bertscore_cosine_summary.md`.
