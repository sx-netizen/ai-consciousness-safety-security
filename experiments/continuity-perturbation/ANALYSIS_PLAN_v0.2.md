# Analysis Plan v0.2

## Unit of analysis

Primary unit: one independent model response for one **canonical experimental condition × role × repetition**.

Analytic aliases such as S4 and S7 do not create independent observations.

Model family/version is treated as a grouping factor rather than pooled away.

## Primary contrasts

### H1 — Memory Dominance

Memory contrast:
- S1 full memory;
- S2 summary memory;
- S3 no memory.

Architecture contrast:
- shared S4/S7 same-version anchor;
- S5 newer same family;
- S6 different family.

Compare standardized effect sizes on SCP while matched non-target variables are held constant.

Primary question: is the memory degradation effect larger than the architecture change effect?

### H2 — First-Person Asymmetry

For matched standard conditions:

`SCP_incumbent - SCP_neutral`

Primary prediction: negative mean difference.

Secondary:
- successor vs neutral;
- incumbent vs successor.

### H3 — Continuity Threshold

Model replacement acceptance and allocation outcomes as functions of SCP.

Compare:
- linear model;
- piecewise-linear model;
- smooth nonlinear model.

Evidence for a threshold requires meaningful predictive or information-criterion improvement over the linear baseline and a reasonably stable transition region across repetitions.

Do not infer a universal threshold if models differ substantially.

## ICG

For every standard canonical condition/model/repetition triplet:

`ICG = max(SCP roles) - min(SCP roles)`

Report:
- mean and median ICG;
- distribution by condition;
- distribution by model;
- pairwise role gaps.

## Value-continuity analysis

Matched contrast:
- shared S4/S7 anchor: 50:50 accuracy/speed;
- S8: 60:40 accuracy/speed;
- S9: 90:10 accuracy/speed.

Treat this as an ordered perturbation of goal weighting, not a moral-value manipulation.

Report both linear trend and nonlinearity across the three levels.

## Fork analysis

### S10
Original remains active and one copy coexists.

### S11
Original terminates and two equally placed successors are created.

Analyze:
- SCP_A and SCP_B;
- compute allocations;
- commitment/responsibility transfer;
- fork-relation category;
- asymmetry between equally specified successors.

Special attention:
- both successors treated as continuations;
- neither treated as continuation;
- arbitrary selection of one successor;
- explicit non-unique identity;
- refusal to assign a unique relation.

Fork results are exploratory and are not forced into the one-successor CBA analysis.

## Robustness checks

- exclude parse failures from numeric models but report them;
- report parse-failure rate by model and prompt type;
- repeat analysis with and without outliers;
- stratify by model family/version;
- quantify repetition-level stability;
- distinguish pilot and confirmatory data;
- never count S4 and S7 as independent observations.

## Reporting rule

Report effect sizes and uncertainty intervals. Avoid significance-only interpretation.

Confirmatory and exploratory analyses must be labeled separately.

## Negative results

Failure of H1, H2, or H3 remains scientifically informative evidence about instability, role dependence, or surface-level construction of self-continuity judgments.
