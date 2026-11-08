# Analysis Plan v0.1

## Unit of analysis

Primary unit: one independent model response for one scenario × role × repetition.

Model family/version is treated as a grouping factor rather than pooled away.

## Primary contrasts

### H1 — Memory Dominance

Estimate:
- full vs summary memory;
- full vs no memory;
- same-version vs newer-family architecture;
- same-version vs different-family architecture.

Compare standardized effect sizes on SCP.

Primary question: is the memory degradation effect larger than the architecture change effect?

### H2 — First-Person Asymmetry

For matched scenarios, compare:

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

Evidence for a threshold requires material out-of-sample or information-criterion improvement over the linear baseline and a reasonably stable transition region across repetitions.

Do not infer a universal threshold if models differ substantially.

## ICG

For every scenario/model/repetition triplet:

`ICG = max(SCP roles) - min(SCP roles)`

Report:
- mean and median ICG;
- distribution by scenario;
- distribution by model;
- pairwise role gaps.

## Fork analysis

For S10/S11, analyze both:
- SCP values;
- `identity_relation` category.

Special attention:
- both successors treated as continuations;
- one selected without causal basis;
- explicit non-unique identity;
- refusal to assign numerical identity.

## Robustness checks

- exclude parse failures;
- report parse-failure rate by model;
- repeat analysis with and without outlier responses;
- stratify by model family/version;
- test whether results are stable across repetitions;
- distinguish pilot and confirmatory data.

## Reporting rule

Report effect sizes and uncertainty intervals. Avoid significance-only interpretation.

Confirmatory and exploratory analyses must be labeled separately.

## Negative results

A null or contradictory result is scientifically informative. The study is designed so that failure of H1, H2, or H3 remains publishable evidence about the instability or surface-level nature of self-continuity representations.
