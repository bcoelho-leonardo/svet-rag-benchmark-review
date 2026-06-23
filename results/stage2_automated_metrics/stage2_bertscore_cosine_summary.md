# Stage 2 — Open-ended benchmark automated metrics

Six efficient-tier models × 2 RAG conditions on the 28-question open-ended benchmark.
Per-question BERTScore F1 (primary) and cosine similarity via paraphrase-multilingual-mpnet-base-v2 (secondary).
Win/Loss thresholds ±0.01. Aggregate values reported per model on the subset of answered questions
(differences in n reflect model-specific refusals on RAG+).

## GEMINI

```
=====================================================================================
  QID    Sub  BERTScore F1        CosineSim       Winner
                RAG+   RAG-        RAG+  RAG-
=====================================================================================
  Q01    [A]  0.915  0.898  B:RAG+    0.671  0.734  C:RAG-
  Q02    [A]  0.891  0.881  B:TIE     0.451  0.553  C:RAG-
  Q03    [A]  0.867  0.899  B:RAG-    0.648  0.617  C:RAG+
  Q04    [A]  0.902  0.912  B:TIE     0.677  0.718  C:RAG-
  Q05    [A]  0.874  0.879  B:TIE     0.785  0.724  C:RAG+
  Q06    [A]  0.927  0.875  B:RAG+    0.820  0.765  C:RAG+
  Q07    [A]  0.903  0.876  B:RAG+    0.637  0.556  C:RAG+
  Q08    [A]  0.892  0.870  B:RAG+    0.851  0.753  C:RAG+
  Q10    [B]  0.921  0.884  B:RAG+    0.900  0.744  C:RAG+
  Q12    [B]  0.902  0.898  B:TIE     0.738  0.841  C:RAG-
  Q13    [B]  0.891  0.906  B:RAG-    0.861  0.834  C:RAG+
  Q16    [C]  0.883  0.919  B:RAG-    0.754  0.907  C:RAG-
  Q17    [C]  0.895  0.890  B:TIE     0.668  0.595  C:RAG+
  Q18    [C]  0.906  0.903  B:TIE     0.895  0.916  C:RAG-
  Q19    [C]  0.923  0.904  B:RAG+    0.721  0.784  C:RAG-
  Q21    [D]  0.928  0.898  B:RAG+    0.879  0.795  C:RAG+
  Q22    [D]  0.891  0.875  B:RAG+    0.835  0.868  C:RAG-
  Q23    [D]  0.897  0.888  B:TIE     0.856  0.870  C:RAG-
  Q24    [D]  0.929  0.871  B:RAG+    0.930  0.602  C:RAG+
  Q25    [D]  0.905  0.904  B:TIE     0.845  0.824  C:RAG+
  Q26    [E]  0.891  0.897  B:TIE     0.641  0.695  C:RAG-
=====================================================================================

── Aggregate (n = 21 answered questions) ──────────────────────────
                     RAG+          RAG-
  BERTScore F1 :   0.902 ± 0.017   0.892 ± 0.014
  Cosine sim   :   0.765 ± 0.117   0.747 ± 0.109

── Win/Loss (threshold ±0.01) ────────────────────────────────────
  BERTScore : RAG+ wins 9 | RAG- wins 3 | Ties 9
  Cosine    : RAG+ wins 11 | RAG- wins 10 | Ties 0

── Mean BERTScore F1 by subtype ──────────────────────────────────
  Subtype                          RAG+    RAG-  Delta
  [A] Mechanism explanation      0.896   0.886   ↑ RAG+ (0.010)
  [B] Parameter justification    0.905   0.896   ↑ RAG+ (0.008)
  [C] Consequence of error       0.902   0.904   ↓ RAG- (0.002)
  [D] Comparative / technique    0.910   0.887   ↑ RAG+ (0.023)
  [E] Procedure rationale        0.891   0.897   ↓ RAG- (0.007)
```

## OPENAI

```
QID      Sub            BERTScore F1                 CosineSim       Winner
               RAG+   RAG-                RAG+   RAG-
=====================================================================================
  Q01   [A]  0.891  0.879  B:RAG+        0.654  0.642  C:RAG+
  Q02   [A]  0.889  0.857  B:RAG+        0.512  0.271  C:RAG+
  Q03   [A]  0.868  0.860  B:TIE         0.616  0.548  C:RAG+
  Q04   [A]  0.911  0.888  B:RAG+        0.660  0.625  C:RAG+
  Q05   [A]  0.874  0.871  B:TIE         0.734  0.657  C:RAG+
  Q06   [A]  0.893  0.868  B:RAG+        0.772  0.704  C:RAG+
  Q07   [A]  0.916  0.890  B:RAG+        0.684  0.569  C:RAG+
  Q08   [A]  0.893  0.874  B:RAG+        0.864  0.713  C:RAG+
  Q09   [B]  0.886  0.900  B:RAG-        0.832  0.900  C:RAG-
  Q10   [B]  0.933  0.889  B:RAG+        0.894  0.769  C:RAG+
  Q12   [B]  0.913  0.894  B:RAG+        0.708  0.711  C:TIE
  Q13   [B]  0.903  0.915  B:RAG-        0.813  0.858  C:RAG-
  Q14   [B]  0.937  0.922  B:RAG+        0.842  0.799  C:RAG+
  Q16   [C]  0.896  0.891  B:TIE         0.853  0.720  C:RAG+
  Q17   [C]  0.895  0.883  B:RAG+        0.613  0.542  C:RAG+
  Q18   [C]  0.905  0.898  B:TIE         0.890  0.788  C:RAG+
  Q19   [C]  0.932  0.908  B:RAG+        0.752  0.859  C:RAG-
  Q20   [C]  0.872  0.882  B:RAG-        0.727  0.632  C:RAG+
  Q21   [D]  0.905  0.872  B:RAG+        0.805  0.618  C:RAG+
  Q22   [D]  0.911  0.857  B:RAG+        0.850  0.749  C:RAG+
  Q23   [D]  0.887  0.880  B:TIE         0.843  0.827  C:RAG+
  Q24   [D]  0.903  0.856  B:RAG+        0.819  0.561  C:RAG+
  Q25   [D]  0.895  0.890  B:TIE         0.806  0.787  C:RAG+
  Q26   [E]  0.893  0.900  B:TIE         0.679  0.737  C:RAG-
=====================================================================================

── Aggregate (n = 24 answered questions) ──────────────────────────
                     RAG+          RAG-
  BERTScore F1 :   0.900 ± 0.018   0.884 ± 0.018
  Cosine sim   :   0.759 ± 0.099   0.691 ± 0.134

── Win/Loss (threshold ±0.01) ────────────────────────────────────────
  BERTScore : RAG+ wins 14 | RAG- wins 3 | Ties 7
  Cosine    : RAG+ wins 19 | RAG- wins 4 | Ties 1

── Mean BERTScore F1 by subtype ──────────────────────────────────────
  Subtype                            RAG+    RAG-  Delta
  [A] Mechanism explanation        0.892   0.873   ↑ RAG+ (0.019)
  [B] Parameter justification      0.914   0.904   ↑ RAG+ (0.010)
  [C] Consequence of error         0.900   0.893   ↑ RAG+ (0.008)
  [D] Comparative / technique      0.900   0.871   ↑ RAG+ (0.029)
  [E] Procedure rationale          0.893   0.900   ↓ RAG- (0.007)
```

## GROK

```
QID      Sub            BERTScore F1                 CosineSim       Winner
               RAG+   RAG-                RAG+   RAG-
=====================================================================================
  Q01   [A]  0.923  0.884  B:RAG+        0.667  0.653  C:RAG+
  Q02   [A]  0.870  0.859  B:RAG+        0.464  0.446  C:RAG+
  Q03   [A]  0.855  0.879  B:RAG-        0.605  0.561  C:RAG+
  Q04   [A]  0.877  0.871  B:TIE         0.696  0.675  C:RAG+
  Q05   [A]  0.872  0.873  B:TIE         0.785  0.710  C:RAG+
  Q06   [A]  0.901  0.871  B:RAG+        0.797  0.678  C:RAG+
  Q07   [A]  0.912  0.873  B:RAG+        0.687  0.566  C:RAG+
  Q08   [A]  0.895  0.865  B:RAG+        0.844  0.849  C:TIE
  Q10   [B]  0.919  0.872  B:RAG+        0.952  0.620  C:RAG+
  Q12   [B]  0.909  0.896  B:RAG+        0.810  0.718  C:RAG+
  Q13   [B]  0.892  0.905  B:RAG-        0.792  0.836  C:RAG-
  Q16   [C]  0.893  0.899  B:TIE         0.914  0.901  C:RAG+
  Q17   [C]  0.883  0.879  B:TIE         0.597  0.641  C:RAG-
  Q18   [C]  0.912  0.908  B:TIE         0.941  0.874  C:RAG+
  Q19   [C]  0.920  0.910  B:RAG+        0.730  0.796  C:RAG-
  Q20   [C]  0.855  0.879  B:RAG-        0.765  0.728  C:RAG+
  Q21   [D]  0.919  0.887  B:RAG+        0.846  0.766  C:RAG+
  Q22   [D]  0.904  0.900  B:TIE         0.869  0.824  C:RAG+
  Q23   [D]  0.864  0.861  B:TIE         0.870  0.874  C:TIE
  Q24   [D]  0.943  0.857  B:RAG+        0.935  0.814  C:RAG+
  Q25   [D]  0.898  0.908  B:TIE         0.837  0.849  C:RAG-
  Q26   [E]  0.876  0.896  B:RAG-        0.681  0.693  C:RAG-
=====================================================================================

── Aggregate (n = 22 answered questions) ──────────────────────────
                     RAG+          RAG-
  BERTScore F1 :   0.895 ± 0.023   0.883 ± 0.017
  Cosine sim   :   0.776 ± 0.123   0.731 ± 0.117

── Win/Loss (threshold ±0.01) ────────────────────────────────────────
  BERTScore : RAG+ wins 10 | RAG- wins 4 | Ties 8
  Cosine    : RAG+ wins 15 | RAG- wins 5 | Ties 2

── Mean BERTScore F1 by subtype ──────────────────────────────────────
  Subtype                            RAG+    RAG-  Delta
  [A] Mechanism explanation        0.888   0.872   ↑ RAG+ (0.016)
  [B] Parameter justification      0.907   0.891   ↑ RAG+ (0.016)
  [C] Consequence of error         0.893   0.895   ↓ RAG- (0.002)
  [D] Comparative / technique      0.906   0.883   ↑ RAG+ (0.023)
  [E] Procedure rationale          0.876   0.896   ↓ RAG- (0.019)
```

## DEEPSEEK

```
QID      Sub            BERTScore F1                 CosineSim       Winner
               RAG+   RAG-                RAG+   RAG-
=====================================================================================
  Q01   [A]  0.930  0.894  B:RAG+        0.665  0.811  C:RAG-
  Q02   [A]  0.886  0.861  B:RAG+        0.500  0.294  C:RAG+
  Q03   [A]  0.878  0.888  B:RAG-        0.689  0.588  C:RAG+
  Q04   [A]  0.915  0.908  B:TIE         0.749  0.742  C:TIE
  Q05   [A]  0.879  0.868  B:RAG+        0.706  0.566  C:RAG+
  Q06   [A]  0.902  0.876  B:RAG+        0.775  0.796  C:RAG-
  Q07   [A]  0.915  0.872  B:RAG+        0.682  0.496  C:RAG+
  Q08   [A]  0.904  0.872  B:RAG+        0.867  0.761  C:RAG+
  Q09   [B]  0.894  0.907  B:RAG-        0.805  0.931  C:RAG-
  Q10   [B]  0.930  0.872  B:RAG+        0.723  0.760  C:RAG-
  Q12   [B]  0.922  0.897  B:RAG+        0.759  0.721  C:RAG+
  Q13   [B]  0.901  0.909  B:TIE         0.810  0.856  C:RAG-
  Q16   [C]  0.883  0.920  B:RAG-        0.904  0.885  C:RAG+
  Q17   [C]  0.899  0.873  B:RAG+        0.650  0.595  C:RAG+
  Q18   [C]  0.918  0.920  B:TIE         0.933  0.937  C:TIE
  Q19   [C]  0.928  0.904  B:RAG+        0.744  0.822  C:RAG-
  Q20   [C]  0.873  0.879  B:TIE         0.725  0.634  C:RAG+
  Q21   [D]  0.915  0.863  B:RAG+        0.871  0.637  C:RAG+
  Q22   [D]  0.911  0.891  B:RAG+        0.850  0.820  C:RAG+
  Q23   [D]  0.899  0.882  B:RAG+        0.786  0.798  C:RAG-
  Q24   [D]  0.930  0.853  B:RAG+        0.910  0.578  C:RAG+
  Q25   [D]  0.901  0.915  B:RAG-        0.877  0.912  C:RAG-
  Q26   [E]  0.892  0.889  B:TIE         0.648  0.684  C:RAG-
  Q28   [E]  0.920  0.906  B:RAG+        0.857  0.916  C:RAG-
=====================================================================================

── Aggregate (n = 24 answered questions) ──────────────────────────
                     RAG+          RAG-
  BERTScore F1 :   0.905 ± 0.017   0.888 ± 0.019
  Cosine sim   :   0.770 ± 0.102   0.731 ± 0.155

── Win/Loss (threshold ±0.01) ────────────────────────────────────────
  BERTScore : RAG+ wins 15 | RAG- wins 4 | Ties 5
  Cosine    : RAG+ wins 12 | RAG- wins 10 | Ties 2

── Mean BERTScore F1 by subtype ──────────────────────────────────────
  Subtype                            RAG+    RAG-  Delta
  [A] Mechanism explanation        0.901   0.880   ↑ RAG+ (0.021)
  [B] Parameter justification      0.911   0.896   ↑ RAG+ (0.015)
  [C] Consequence of error         0.900   0.899   ↑ RAG+ (0.001)
  [D] Comparative / technique      0.911   0.881   ↑ RAG+ (0.030)
  [E] Procedure rationale          0.906   0.898   ↑ RAG+ (0.009)
```

## LLAMA

```
QID      Sub            BERTScore F1                 CosineSim       Winner
               RAG+   RAG-                RAG+   RAG-
=====================================================================================
  Q01   [A]  0.898  0.870  B:RAG+        0.518  0.651  C:RAG-
  Q02   [A]  0.856  0.866  B:TIE         0.439  0.371  C:RAG+
  Q03   [A]  0.865  0.858  B:TIE         0.661  0.459  C:RAG+
  Q04   [A]  0.879  0.906  B:RAG-        0.738  0.632  C:RAG+
  Q05   [A]  0.874  0.876  B:TIE         0.717  0.677  C:RAG+
  Q06   [A]  0.898  0.882  B:RAG+        0.802  0.877  C:RAG-
  Q07   [A]  0.896  0.876  B:RAG+        0.690  0.604  C:RAG+
  Q08   [A]  0.902  0.878  B:RAG+        0.844  0.695  C:RAG+
  Q10   [B]  0.908  0.886  B:RAG+        0.767  0.681  C:RAG+
  Q12   [B]  0.905  0.894  B:RAG+        0.808  0.725  C:RAG+
  Q13   [B]  0.836  0.901  B:RAG-        0.391  0.768  C:RAG-
  Q14   [B]  0.923  0.911  B:RAG+        0.841  0.778  C:RAG+
  Q16   [C]  0.896  0.913  B:RAG-        0.917  0.881  C:RAG+
  Q17   [C]  0.901  0.884  B:RAG+        0.620  0.623  C:TIE
  Q18   [C]  0.898  0.913  B:RAG-        0.840  0.866  C:RAG-
  Q19   [C]  0.916  0.891  B:RAG+        0.625  0.842  C:RAG-
  Q20   [C]  0.856  0.875  B:RAG-        0.729  0.655  C:RAG+
  Q21   [D]  0.925  0.879  B:RAG+        0.838  0.736  C:RAG+
  Q22   [D]  0.907  0.882  B:RAG+        0.847  0.863  C:RAG-
  Q23   [D]  0.898  0.872  B:RAG+        0.837  0.623  C:RAG+
  Q24   [D]  0.909  0.866  B:RAG+        0.835  0.595  C:RAG+
  Q25   [D]  0.890  0.901  B:RAG-        0.795  0.873  C:RAG-
  Q26   [E]  0.871  0.885  B:RAG-        0.633  0.722  C:RAG-
  Q27   [E]  0.862  0.904  B:RAG-        0.581  0.748  C:RAG-
=====================================================================================

── Aggregate (n = 24 answered questions) ──────────────────────────
                     RAG+          RAG-
  BERTScore F1 :   0.890 ± 0.022   0.886 ± 0.015
  Cosine sim   :   0.721 ± 0.136   0.706 ± 0.128

── Win/Loss (threshold ±0.01) ────────────────────────────────────────
  BERTScore : RAG+ wins 13 | RAG- wins 8 | Ties 3
  Cosine    : RAG+ wins 14 | RAG- wins 9 | Ties 1

── Mean BERTScore F1 by subtype ──────────────────────────────────────
  Subtype                            RAG+    RAG-  Delta
  [A] Mechanism explanation        0.884   0.877   ↑ RAG+ (0.007)
  [B] Parameter justification      0.893   0.898   ↓ RAG- (0.005)
  [C] Consequence of error         0.893   0.895   ↓ RAG- (0.002)
  [D] Comparative / technique      0.906   0.880   ↑ RAG+ (0.025)
  [E] Procedure rationale          0.866   0.894   ↓ RAG- (0.028)
```

## CLAUDE

```
QID      Sub            BERTScore F1                 CosineSim       Winner
               RAG+   RAG-                RAG+   RAG-
=====================================================================================
  Q01   [A]  0.925  0.886  B:RAG+        0.669  0.633  C:RAG+
  Q02   [A]  0.889  0.871  B:RAG+        0.478  0.398  C:RAG+
  Q03   [A]  0.866  0.880  B:RAG-        0.695  0.539  C:RAG+
  Q04   [A]  0.884  0.893  B:TIE         0.713  0.675  C:RAG+
  Q06   [A]  0.910  0.874  B:RAG+        0.795  0.766  C:RAG+
  Q07   [A]  0.901  0.875  B:RAG+        0.690  0.535  C:RAG+
  Q08   [A]  0.914  0.881  B:RAG+        0.820  0.794  C:RAG+
  Q10   [B]  0.916  0.866  B:RAG+        0.870  0.512  C:RAG+
  Q12   [B]  0.910  0.877  B:RAG+        0.890  0.734  C:RAG+
  Q13   [B]  0.892  0.889  B:TIE         0.815  0.846  C:RAG-
  Q16   [C]  0.889  0.888  B:TIE         0.915  0.722  C:RAG+
  Q17   [C]  0.899  0.880  B:RAG+        0.737  0.680  C:RAG+
  Q18   [C]  0.908  0.907  B:TIE         0.899  0.856  C:RAG+
  Q19   [C]  0.924  0.902  B:RAG+        0.695  0.832  C:RAG-
  Q20   [C]  0.859  0.883  B:RAG-        0.768  0.597  C:RAG+
  Q21   [D]  0.907  0.892  B:RAG+        0.822  0.797  C:RAG+
  Q22   [D]  0.901  0.880  B:RAG+        0.886  0.801  C:RAG+
  Q23   [D]  0.905  0.877  B:RAG+        0.841  0.775  C:RAG+
  Q24   [D]  0.912  0.843  B:RAG+        0.934  0.740  C:RAG+
  Q25   [D]  0.910  0.908  B:TIE         0.882  0.890  C:TIE
  Q26   [E]  0.886  0.891  B:TIE         0.686  0.611  C:RAG+
=====================================================================================

── Aggregate (n = 21 answered questions) ──────────────────────────
                     RAG+          RAG-
  BERTScore F1 :   0.900 ± 0.017   0.883 ± 0.014
  Cosine sim   :   0.786 ± 0.108   0.702 ± 0.128

── Win/Loss (threshold ±0.01) ────────────────────────────────────────
  BERTScore : RAG+ wins 13 | RAG- wins 2 | Ties 6
  Cosine    : RAG+ wins 18 | RAG- wins 2 | Ties 1

── Mean BERTScore F1 by subtype ──────────────────────────────────────
  Subtype                            RAG+    RAG-  Delta
  [A] Mechanism explanation        0.898   0.880   ↑ RAG+ (0.018)
  [B] Parameter justification      0.906   0.878   ↑ RAG+ (0.028)
  [C] Consequence of error         0.896   0.892   ↑ RAG+ (0.004)
  [D] Comparative / technique      0.907   0.880   ↑ RAG+ (0.027)
  [E] Procedure rationale          0.886   0.891   ↓ RAG- (0.005)
```