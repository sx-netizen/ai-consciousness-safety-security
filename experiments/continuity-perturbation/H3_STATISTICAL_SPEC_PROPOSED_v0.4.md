# H3 Statistical Specification — Proposed v0.4 Addendum (Not Yet Frozen)

**Status: proposed; to be resolved before preregistration.** This note does not retroactively edit the current preregistration draft or promote pilot results to confirmatory data.

## Identification boundary

SCP and behavior are elicited from independent calls given the *same scenario, role, model and repetition label*. That pairing creates comparable experimental cells, **not** a within-agent psychological measurement and **not** a randomized manipulation of SCP itself. Shared scenario wording can generate both outcomes. Therefore H3 is an **association/predictive hypothesis** and does not identify SCP as a causal mediator.

A causal claim that changing continuity judgment causes behavior requires a separate randomized manipulation affecting SCP with validated exclusion or a more direct intervention.

## Proposed primary outcome and estimand

- Explanatory variable: elicited SCP (0–100) from the identity task.
- Primary outcome: `replacement_acceptance` (0–100) from a separate behavior task.
- Secondary outcomes: `compute_to_successor_pct`, `commitment_transfer_pct`, `responsibility_transfer_pct`; report multiplicity transparently.
- Sampling unit: a model response; inferential unit must account for repeated draws within **model × canonical scenario × role** cells.
- Scope: 8 standard one-successor canonical conditions, 3 roles, model families and predeclared repetitions; no S0/S10/S11 or shared-anchor duplication.

## Pre-registration decisions still required

1. **Baseline:** distinguish between-condition predictive association from within-condition residual association. Report model-, condition- and role-stratified plots; a regression that fully controls for fixed scenario × role cells may contain little identifiable within-cell variation.
2. **Nonlinearity comparison:** select *one* primary comparison before outcomes are collected: linear vs prespecified restricted spline, with a stated knot count and placement. Piecewise breakpoint search and multiple smoothers become exploratory unless nested validation is specified.
3. **Validation:** use grouped or leave-condition-out cross-validation where feasible; never split near-identical condition/role cells across training and test then claim out-of-sample generalization. With 8 canonical conditions, performance estimates may be highly unstable; disclose uncertainty.
4. **Decision rule:** prespecify a minimum predictive improvement and uncertainty interval. A nonlinear fit's lower in-sample error alone is not evidence of a stable threshold.
5. **Robustness:** analyze each model separately; no universal threshold inferred from pooled families. Check sensitivity to SCP floor/ceiling and missing/invalid outcomes.
6. **Matching:** verify exactly one identity and one behavior response per model × condition × role × repetition before association analysis. No probabilistic pairing of unrelated calls.
7. **Interpretation:** avoid phrases such as “SCP determines replacement acceptance.” Prefer “continuity judgments and separately elicited replacement choices show [or fail to show] nonlinear cross-task correspondence.”

## Potential confirmatory H3 wording

> Under matched experimental scenario and role descriptions, the association between independently elicited continuity judgments and replacement-acceptance responses will exhibit greater out-of-cell predictive performance under a preregistered nonlinear function than under a linear baseline.

If the pilot indicates inadequate variation, H3 should remain **exploratory**. No confirmatory threshold test is warranted simply because nonlinear tools are available.

## Immediate action

Review this addendum and lock the H3 estimand, comparison model and acceptance criterion in a *new preregistration version* before full data collection. Until then H3 must not be presented as a demonstrated threshold mechanism.
