# LLM generation date range

All commercial LLM API calls analysed in this manuscript were generated between **3 March 2026 and 7 March 2026** using each provider's official Python SDK.

This single window covers all three evaluation stages:

- Stage 1 — 50-question MCQ benchmark, 12 models x 2 RAG conditions at T = 0, plus 6 efficient-tier models x 2 RAG conditions at T = 0.7, N = 3 runs per cell.
- Stage 2 — 28-question open-ended benchmark, 6 efficient-tier models x 2 RAG conditions, T = 0.
- Stage 3 — paired open-ended responses (RAG+ and RAG-) for the same 6 efficient-tier models, generated for blind human evaluation.

The raw output files include the model identifier string, RAG condition, temperature, run number where applicable, raw output, parsed output, retrieved context where available, and scoring fields. Where exact per-call timestamps were not logged, the date range above defines the execution window for the corresponding benchmark stage.
