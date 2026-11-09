# Dates of model-response generation

Per the authors' records (consistent with SI Section S12):

| Item | Date |
|---|---|
| Stage 1 model responses (50 MCQs; T = 0 and T = 0.7 runs) | 3 and 4 March 2026 |
| Stage 2 model responses (28 open-ended questions) | 6 March 2026 |
| Stage 2 Perplexity Sonar judge | 7 March 2026 |
| Reference-aware judge and revision analyses | 6 October 2026 (judge); October–November 2026 (analyses) |

The saved output files carry matching modification times, with one exception: the Llama-4-Scout Stage 1
RAG+ T = 0 file carries a modification time of 1 April 2026. Per-call timestamps were not logged. Stage 3 reused the
Stage 2 responses without additional generation. The original March 2026 software environment was not logged
(see `requirements.txt` and SI Section S12).
