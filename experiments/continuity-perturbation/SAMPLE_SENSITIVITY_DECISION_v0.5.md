# Zero-Cost Sample-Sensitivity Decision Note — CPB v0.5

**Status: design simulation, not empirical evidence; does not freeze a sample size.**

`power_simulation.py` runs a seeded, zero-provider-call simulation for the two currently proposed primary contrasts:

- H1: `SCP(S6) - SCP(S3)`, positive when complete autobiographical memory loss is described as more disruptive than a different-model-family description.
- H2: `SCP(incumbent) - SCP(neutral)`, with eight canonical scenario gaps aggregated **within each repetition** before any uncertainty interval is computed.

It compares 5, 10 and 20 *stochastic repetitions within each fixed model*, across assumed true effect magnitudes 0/5/10/20 SCP points. The simulation explicitly includes a shared role-framing noise term for H2; treating eight scenarios as eight fully independent repetitions would materially overstate effective sample size.

## Fixed assumptions

- Per-scenario H1 response noise is Gaussian with SD 15 SCP points; contrasts subtract independent condition responses.
- H2 includes Gaussian shared role-framing noise SD 10 and additional per-scenario residual noise SD 15; condition gaps are averaged once per repetition.
- The 95% uncertainty interval is a Student-t interval over repetition summaries, conditional on stable model behavior and normality.
- A directional detection is registered if a two-sided 95% interval lies entirely above zero (H1) or below zero (H2).
- No real observed AI model variance is available, so none of these numerical assumptions is empirically calibrated.

## Decision discipline

1. Read CI artifact `acss-cpb-statistical-sensitivity` for the complete table and record its seed and parameters.
2. If a five-repetition design is weak under plausible noise, describe outcomes as exploratory precision estimates rather than claiming a broadly powered confirmatory test.
3. Raising repetitions can improve precision **within a fixed model configuration**, but it cannot create more independent model families or eliminate version drift, common prompt framing, ceiling effects, or data invalidity.
4. Never select a repetition count based on which actual observed model responses look significant. A no-cost diagnostic model sample would need a separately verified free plan and a versioned exploratory procedure.
5. H3 remains exploratory: seven jointly observed scenario conditions are not a reliable basis for searching many nonlinear thresholds.

**No billable calls, model outputs, changes to the 50-prompt core, or frozen protocol updates are authorized by this analysis.**
