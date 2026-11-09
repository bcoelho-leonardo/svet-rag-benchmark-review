# Provenance and Sensitivity Analysis Freeze

**Manuscript:** *Retrieval augmentation improves reliability of large language models for specialist instrumentation: a three-stage evaluation using the scanning vibrating electrode technique*  
**Manuscript ID:** DD-ART-06-2026-000414  
**Freeze date:** 2026-10-06  
**Status:** Final pre-computation freeze. No provenance-based sensitivity recomputation had been performed when this version was committed.

## Purpose

This manifest records, before recomputation, the provenance criteria, item-level treatment decisions, and analysis rules for the post-hoc robustness analyses addressing Referee 1's concern about benchmark construction and ground-truth authorship.

The primary experiments, original question banks, original model generations, and originally reported results remain unchanged. No model-generation API calls are required for these provenance-based analyses.

The provenance audit improves auditability but **does not replace independent expert validation**.

## Disclosure about prior knowledge of results

Item-level error patterns from the primary analysis were already known when this audit was performed. Exclusion and reference-edit criteria were defined from documentary provenance, scope, and question formulation only. The sets below were fixed before recomputation.

Two examples help demonstrate that the audit was not performance-selected:

- **S1-Q34** is excluded in the conservative formulation sensitivity even though RAG improved performance on that item.
- **S1-Q39** is retained despite being one of the largest residual RAG+ error clusters, because its central scientific content is independently supported.

No item is to be added to or removed from the frozen sets because of the sensitivity results.

## Provenance hierarchy and definition of borderline items

Independent support was assessed using a consistent hierarchy:

1. **Level 1:** manufacturer/operator documentation and identifiable peer-reviewed literature.
2. **Level 2:** documented training/procedure records describing actual instrument or laboratory practice.
3. **Level 3:** PI-curated or synthesized KB materials (e.g. expert Q&A, community summaries, compiled guides).

For consistency, **all items whose strongest initial support was Level 2 or Level 3, or whose wording raised an explicit scope/formulation concern, were treated as borderline and subjected to targeted manufacturer/literature verification before this freeze**. Thus, an item was not classified as curator-only merely because the independent source was not already present as a standalone KB chunk.

Key independent checks include:

- Bastos AC, Quevedo MC, Karavai OV, Ferreira MGS. *Review—On the Application of the Scanning Vibrating Electrode Technique (SVET) to Corrosion Research.* J. Electrochem. Soc. 164 (2017) C973-C990. DOI: 10.1149/2.0431714jes.
- Akid R, Garma M. *Scanning vibrating reference electrode technique: a calibration study to evaluate the optimum operating parameters for maximum signal detection of point source activity.* Electrochim. Acta 49 (2004) 2871-2879. DOI: 10.1016/j.electacta.2004.01.069.
- BioLogic technical guidance on selection of scanning probe electrochemistry techniques, including sample electrical-connection requirements for LEIS, SDC and SVET.

The Bastos review was checked directly and explicitly states that:
- to avoid current overestimation, the probe should be at least four times the **vibration amplitude** from the source;
- positive current corresponds to anodic activity under the conventional SVET sign convention;
- SVET misses currents flowing between anodic and cathodic regions below the measurement height;
- vibration/lock-in detection substantially improves signal-to-noise relative to SRET;
- 1 nF can be acceptable for common AE tips, while the acceptable minimum is instrument/noise dependent.

The AE operator manual separately describes approximately 2 nF as a good operational capacitance criterion. This difference is treated as instrument/practice dependence rather than as evidence that either source is false.

## Revision history before recomputation

Several provisional classifications changed during the audit **before any sensitivity result was calculated**. They are recorded here so that the final freeze is auditable rather than appearing to have been chosen after the fact.

- **S1-Q8:** provisional curator-only candidate -> independently supported. Direct verification of Bastos et al. confirmed that the four-times rule refers to **vibration amplitude**, not electrode diameter.
- **S1-Q14:** provisional curator-only candidate -> independently supported. Bastos et al. explicitly state positive/anodic and negative/cathodic current convention.
- **S1-Q32:** provisional curator-only candidate -> independently supported. Bastos et al. explicitly state that SVET misses currents flowing below the measurement height.
- **S1-Q42 / S1-Q50:** provisional curator-only candidates -> independently supported by BioLogic technical guidance on electrical-connection requirements and SVET use with naturally active/biological samples.
- **S2-Q01:** provisional deletion-only -> briefly considered unchanged after finding literature support for ~1 nF -> **final deletion-only**. The literature states 1 nF can be acceptable whereas the AE manual uses ~2 nF as a good operational criterion; because the exact threshold is instrument/practice dependent and not needed to answer the question, the numerical parenthetical is removed in the audited reference.
- **S2-Q05 / S2-Q20:** provisional exclusion -> **final deletion-only** after direct verification that the four-times-vibration-amplitude rule and current overestimation are independently supported; only the more detailed unverified demodulation mechanism is removed.
- **S2-Q09:** provisional deletion-only -> **final exclusion** because the question itself asks *why* 150 µm is used as a standard; the documented geometry is valid but the asserted rationale is embedded in the premise.
- **S2-Q21:** provisional exclusion -> **final deletion-only** after independent literature confirmed the SNR advantage of vibrating/lock-in SVET over SRET; the exact ~10× magnitude remains unsupported and is removed.
- **S2-Q22:** provisional exclusion -> **final unchanged** after independent BioLogic documentation confirmed the electrical-connection comparison and use of SVET for naturally active/biological samples.

These revisions were driven only by source verification and question formulation, not by sensitivity-analysis outcomes.

## Stage 1: frozen sensitivity analyses

### S1-A — scope/convention sensitivity

Exclude:

- **S1-Q43**

Reason: the keyed x/z answer reflects an AE-specific coordinate convention and is over-generalized by wording the question as a general SVET convention.

### S1-B — conservative formulation/provenance sensitivity

Exclude:

- **S1-Q15**
- **S1-Q23**
- **S1-Q34**
- **S1-Q43**

Reasons:

- **S1-Q15:** manufacturer documentation supports the usual preamplifier gain and the need to update the software gain when hardware gain changes, but does not support the keyed rationale that the gain should not be altered because it is "factory-calibrated for noise suppression."
- **S1-Q23:** training documentation permits turning the electrode assembly upside down but does not support the trapped-air rationale.
- **S1-Q34:** plausible practitioner criterion for a broken probe, but not directly established in the audited documentation.
- **S1-Q43:** AE-specific coordinate convention presented as a general SVET convention.

### Former S1-C — curated-only/circularity sensitivity

**No S1-C exclusion analysis will be run.**

The provisional candidates S1-Q8, S1-Q14, S1-Q32, S1-Q42 and S1-Q50 were subjected to the same independent-source verification used for all borderline items. Independent support was found for every candidate:

- **S1-Q8:** Bastos et al. explicitly report that the probe should be at least four times the vibration amplitude from the source to avoid signal overestimation.
- **S1-Q14:** Bastos et al. explicitly identify positive current as anodic and negative current as cathodic under the conventional SVET sign convention.
- **S1-Q32:** Bastos et al. explicitly identify missed currents flowing below the probe measurement height as a limitation of quantitative SVET.
- **S1-Q42 / S1-Q50:** BioLogic technical guidance documents that LEIS and SDC require electrical connection to the sample whereas SVET can be used without such connection when the sample is naturally active; it explicitly lists naturally active/corroding and biological samples as SVET applications.

Therefore **none of the proposed Stage-1 circularity candidates relies only on PI-curated Level-3 material once the same external verification standard is applied consistently**. This is an audit finding in its own right; an artificial empty S1-C sensitivity analysis would add no information.

## Stage 2: treatment rules

Three treatments are allowed:

1. **Unchanged:** question and reference are sufficiently independently supported.
2. **Deletion-only/minimal reference cleanup:** the question premise is supported, but an over-specific, instrument-dependent, or insufficiently verified clause in the reference is removed. No new scientific information may be introduced.
3. **Exclude from audited-reference sensitivity:** the concern affects the question premise itself, so editing the answer alone would not solve the provenance problem.

The original 28-question benchmark remains the primary analysis and is not changed.

### S2 items excluded from the audited-reference sensitivity

- **S2-Q09**
- **S2-Q11**
- **S2-Q14**
- **S2-Q17**
- **S2-Q27**
- **S2-Q28**

Reasons:

- **S2-Q09:** 150 µm calibration geometry and ±60 nA calibration current are documented, but the question asks why 150 µm is "used as the standard"; the asserted balance-of-signal-and-safe-standoff rationale is not directly documented.
- **S2-Q11:** 10 mM NaCl was used in training practice, but manufacturer documentation recommends calibration in the experimental solution (or conductivity correction) and also identifies other calibration solutions; "10 mM NaCl is the standard" is over-generalized.
- **S2-Q14:** gas and pressure (compressed air/N2, 30-40 psi, dry) are documented in training notes, but the question embeds an unsupported calibration/environmental-cleaning purpose and rationale.
- **S2-Q17:** literature supports large-amplitude vibration artifacts, including oxygen-transport enhancement and cathodic-current overestimation, but the experimental 25-250 µm range does not establish >25 µm as a universal threshold.
- **S2-Q27:** inversion of the electrode assembly is permitted in training documentation, but the trapped-air/complete-filling rationale is not documented and is built into the "why" question.
- **S2-Q28:** P-47/Program 4/607 °C are documented local training settings, but the question over-generalizes them into a mandatory AE-system requirement.

**Count:** 6 excluded; 22/28 items remain in the audited-reference dataset before response-availability filtering.

### S2 deletion-only/minimal reference-cleanup items

The following reference texts are frozen for the audited-reference sensitivity:

**S2-Q01**  
> Electrodepositing platinum black onto the probe tip dramatically increases its electrochemical surface area, creating a highly capacitive interface that reduces impedance and lowers noise in the measured signal.

Reason: the core mechanism is supported. The original parenthetical "target >1 nF" is removed because the acceptable minimum is instrument/practice dependent: peer-reviewed literature reports ~1 nF as acceptable for common AE tips, whereas the AE manual uses ~2 nF as a good operational criterion.

**S2-Q03**  
> Vibration converts the DC potential gradient above the sample into an AC signal at a known frequency, enabling phase-sensitive lock-in detection that extracts the signal from background noise.

Reason: the lock-in/SNR mechanism is independently supported; the exact "~10x better than static SRET" magnitude is not needed.

**S2-Q05**  
> A probe-sample distance smaller than 4 times the vibration amplitude causes overestimation of local currents.

Reason: the four-times rule and overestimation are independently supported by the SVET literature; the original detailed non-sinusoidal/lock-in mechanism was more specific than the evidence verified.

**S2-Q15**  
> The typical wait-time between measurement points in ASET-LV4 is approximately 0.05 seconds.

Reason: 0.05 s is documented training practice; the original lock-in-stabilization rationale was not directly supported.

**S2-Q20**  
> Setting the probe-sample distance smaller than 4 times the vibration amplitude results in overestimated current densities.

Reason: same independent support as S2-Q05; remove the more specific unverified demodulation mechanism.

**S2-Q21**  
> SVET's vibrating probe combined with lock-in amplifier detection provides a higher signal-to-noise ratio than the static probe used in SRET because phase-sensitive detection rejects noise outside the vibration frequency.

Reason: the SNR advantage over SRET is independently supported; the exact "~10x" magnitude is removed.

**Count:** 6 minimally cleaned references.

### S2 items explicitly retained unchanged after external verification

- **S2-Q06:** spatial-resolution dependence on probe height is independently supported.
- **S2-Q12:** ~1 µA cm^-2 sensitivity in 0.05 M NaCl and conductivity dependence are independently supported.
- **S2-Q18:** the evaporation -> conductivity increase -> current underestimation chain is directly supported by peer-reviewed literature.
- **S2-Q22:** independent manufacturer technical guidance supports the electrical-connection comparison among SVET, LEIS and SDC and SVET applicability to naturally active/biological samples.
- **S2-Q23:** independent literature supports standoff/scan height as the dominant spatial-resolution limitation under the stated conditions.

All other non-excluded Stage-2 items remain unchanged.

Thus, among the 22 retained Stage-2 items, **16 are unchanged and 6 use deletion-only reference cleanup**.

## Stage 2 analysis rules frozen before recomputation

### A. Audited-reference sensitivity

- Use the existing saved model responses only.
- No new model-generation API calls.
- Remove the six excluded S2 items.
- Apply exactly the six reference cleanups above.
- Keep the original BERTScore implementation and encoder/settings unchanged.
- As in the primary analysis, the main audited-reference comparison uses only questions with valid responses under both RAG conditions.
- Report paired per-question RAG+ minus RAG- F1 differences and per-model mean delta.
- Recompute the original >0.01 win/loss classification and McNemar statistic for comparability.
- **For Stage 2**, interpret robustness primarily from effect size and direction, not from whether p remains below 0.05 after sample-size reduction.
- Report whether the audited sensitivity increases, decreases, or leaves approximately unchanged the RAG effect relative to the primary analysis.
- For each deletion-only item, record the direction in which the reference cleanup changes the paired RAG+ minus RAG- delta; do not assume in advance that the cleanup favors or disfavors RAG.

Absolute BERTScore values may shift when references are shortened; the principal comparison is the paired RAG+ versus RAG- delta under identical scoring settings.

### B. Refusal handling: separate sensitivity dimension

Provenance/reference auditing and refusal handling must not be conflated. Refusal treatment addresses Referee 1 Major Comment 3 and will be reported separately/cross-referenced rather than folded into the provenance rebuttal.

The analysis will distinguish:

1. **Original benchmark + primary refusal handling:** refusals excluded, reproducing the submitted analysis.
2. **Audited benchmark + primary refusal handling:** six provenance items removed, six reference cleanups applied, refusals excluded.
3. **Original benchmark + refusal-penalized sensitivity:** all 28 questions retained; a RAG+ refusal is treated as an end-to-end system failure.
4. **Audited benchmark + refusal-penalized sensitivity:** audited 22-question set; refusals on retained items are treated as end-to-end system failures.

For refusal-penalized summaries:
- coverage will be reported explicitly;
- coverage-adjusted mean quality may assign zero contribution to refused answers;
- in win/loss comparisons, a RAG+ refusal with a valid RAG- answer counts against RAG+.

Any exact implementation details used in code must be documented alongside the output and applied identically across models.

S2-Q11 remains present in the original-benchmark refusal analysis but is absent from the audited-benchmark cells because its premise is excluded on provenance grounds.

## PI blindness terminology

The revision should distinguish label blindness from possible perceptual recognition:

- The PI did not inspect or use the randomized X/Y-to-RAG condition mapping while performing the evaluation.
- However, because the PI designed the RAG system and curated/authored substantial portions of the knowledge base, inadvertent recognition of condition-specific content or style cannot be excluded.
- PI results remain reported separately and excluded from pooled external-reviewer statistics.

## Naming convention

From this point onward, all question references must use the prefixes **S1-Qxx** or **S2-Qxx** to prevent ambiguity between the two banks.

## Planned manuscript/SI reporting

The manuscript will:
- replace the over-strong statement that all reference answers were "verified against primary documentation" with a more accurate description of the mixed source basis and the post-hoc provenance audit;
- add a concise provenance/robustness Methods paragraph;
- add a compact Results paragraph reporting sensitivity outcomes;
- describe the Stage-1 scope classification as **post-hoc and PI-derived**;
- state explicitly that the provenance audit does not replace independent expert validation.

The Supplementary Information will include **complete 50-row Stage-1 and 28-row Stage-2 audit tables**, not only flagged items, with at least: item ID, scope/type, strongest evidence level/source, audit issue if any, and final audit status/treatment.

## Freeze rule

This file is the final pre-recomputation decision record. After this commit, item membership and reference edits are not to be changed in response to the observed sensitivity-analysis outcomes. Any later correction must be explicitly documented as a correction to the audit record, with a reason independent of model performance.
