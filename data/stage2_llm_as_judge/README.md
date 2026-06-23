# Stage 2 — supplementary LLM-as-judge evaluation

`results_perplexity_judge.csv` contains the output of the supplementary Perplexity Sonar pairwise judge experiment described in the Supplementary Information.

The judge was shown a question and two candidate answers (one RAG+, one RAG-), identified only by positional code-names. The judge was blind to which response was RAG-grounded and was instructed not to perform external retrieval. Findings (near-random discrimination, positional bias) are discussed in the Supplementary Information; this evaluation is reported as a limitation of automated LLM-as-judge approaches in this domain, not as a primary result.

The exact prompt used is provided at `prompts/stage2/perplexity_judge_prompt.txt`.
