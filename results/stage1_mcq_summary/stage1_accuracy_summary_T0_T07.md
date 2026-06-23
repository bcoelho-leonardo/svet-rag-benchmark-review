# Stage 1 — MCQ benchmark accuracy summary

50-question MCQ benchmark, N = 3 runs per cell, accuracy reported as mean ± SD (%).
Models grouped by provider family. Twelve models tested at T = 0 (frontier + efficient tier);
six efficient-tier models additionally tested at T = 0.7.

## T = 0.0 — all 12 models

| Model | RAG condition | Temperature | N runs | Accuracy |
|---|---|---|---|---|
| gpt-4o-mini | RAG− | 0.0 | 3 | 84.7% ± 2.3% |
| gpt-4o-mini | RAG+ | 0.0 | 3 | 96.7% ± 1.2% |
| gpt-5.2 | RAG− | 0.0 | 3 | 94.7% ± 1.2% |
| gpt-5.2 | RAG+ | 0.0 | 3 | 96.0% ± 0.0% |
| gemini-2.5-flash | RAG− | 0.0 | 3 | 86.0% ± 0.0% |
| gemini-2.5-flash | RAG+ | 0.0 | 3 | 96.0% ± 0.0% |
| gemini-2.5-pro | RAG− | 0.0 | 3 | 90.0% ± 2.0% |
| gemini-2.5-pro | RAG+ | 0.0 | 3 | 96.0% ± 0.0% |
| grok-4-1-fast | RAG− | 0.0 | 3 | 90.7% ± 1.2% |
| grok-4-1-fast | RAG+ | 0.0 | 3 | 94.0% ± 0.0% |
| grok-4 | RAG− | 0.0 | 3 | 92.0% ± 0.0% |
| grok-4 | RAG+ | 0.0 | 3 | 92.7% ± 1.2% |
| deepseek-chat | RAG− | 0.0 | 3 | 90.0% ± 0.0% |
| deepseek-chat | RAG+ | 0.0 | 3 | 96.0% ± 0.0% |
| deepseek-reasoner | RAG− | T = default | 3 | 85.3% ± 1.2% |
| deepseek-reasoner | RAG+ | T = default | 3 | 79.3% ± 3.1% |
| Llama-4-Scout-17B-16E-Instruct | RAG− | 0.0 | 3 | 85.3% ± 1.2% |
| Llama-4-Scout-17B-16E-Instruct | RAG+ | 0.0 | 3 | 100.0% ± 0.0% |
| Llama-4-Maverick-17B-128E-Instruct | RAG− | 0.0 | 3 | 88.0% ± 0.0% |
| Llama-4-Maverick-17B-128E-Instruct | RAG+ | 0.0 | 3 | 98.0% ± 0.0% |
| claude-haiku-4-5 | RAG− | 0.0 | 3 | 96.0% ± 0.0% |
| claude-haiku-4-5 | RAG+ | 0.0 | 3 | 98.0% ± 0.0% |
| claude-sonnet-4-6 | RAG− | 0.0 | 3 | 94.0% ± 0.0% |
| claude-sonnet-4-6 | RAG+ | 0.0 | 3 | 96.0% ± 0.0% |

## T = 0.7 — six efficient-tier models

| Model | RAG condition | Temperature | N runs | Accuracy |
|---|---|---|---|---|
| gpt-4o-mini | RAG− | 0.7 | 3 | 84.7% ± 1.2% |
| gpt-4o-mini | RAG+ | 0.7 | 3 | 96.7% ± 1.2% |
| gemini-2.5-flash | RAG− | 0.7 | 3 | 85.3% ± 1.2% |
| gemini-2.5-flash | RAG+ | 0.7 | 3 | 96.0% ± 0.0% |
| grok-4-1-fast | RAG− | 0.7 | 3 | 89.3% ± 1.2% |
| grok-4-1-fast | RAG+ | 0.7 | 3 | 96.0% ± 0.0% |
| deepseek-chat | RAG− | 0.7 | 3 | 88.7% ± 1.2% |
| deepseek-chat | RAG+ | 0.7 | 3 | 96.0% ± 0.0% |
| Llama-4-Scout-17B-16E-Instruct | RAG− | 0.7 | 3 | 86.0% ± 0.0% |
| Llama-4-Scout-17B-16E-Instruct | RAG+ | 0.7 | 3 | 100.0% ± 0.0% |
| claude-haiku-4-5 | RAG− | 0.7 | 3 | 96.0% ± 2.0% |
| claude-haiku-4-5 | RAG+ | 0.7 | 3 | 96.7% ± 1.2% |





 



