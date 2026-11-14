# CPB v0.5 — Data Handling and Freeze Decision Record

**Draft, not signed or frozen.** No model observations have been collected under this protocol. This note applies to any future approved collection; it is not permission to incur costs.

## Dataset acceptance gates

1. **Provenance:** Keep raw JSONL immutable, with exact study ID, provider/model/version, reasoning setting, prompt body and SHA-256, timestamps, RNG seed, repetition, parse status and all error metadata.
2. **Structural integrity:** Run `audit_dataset.py` against the exact frozen config. A completed dataset must contain precisely one observation for each model × canonical condition × role × task × repetition. Missing, duplicated, unexpected or modified prompt keys must **block a clean integrity designation**. Archive every raw attempt even if re-run.
3. **Failure treatment:** A failed, partial or refused response stays in the denominator for compliance/failure analyses. It is absent, not zero, for SCP and numerical behavior estimates. Never impute from another role, scenario or repetition.
4. **Retries:** No silent retries; an attempted replacement requires a prior declared policy, original record retained and a separate attempt ID. Current runner is append-only, so repeated launches may create duplicate records; integrity audit will flag them.
5. **Synthetic exclusion:** A dry run / synthetic fixture / mock record is never an empirical model observation and cannot pass a clean live-evidence audit.
6. **Role, scenario and version consistency:** Do not pool historical 53-prompt v0.4 designs with the 50-prompt v0.5 candidate without an explicitly version-stratified exploratory analysis. Do not count S1/S4/S7 aliases as separate draws.
7. **Exploratory addenda:** Keep S11 A/B counterbalance separate from the 50 core prompts. Preserve both ordering and output-schema ordering for interpretation.

## Statistical decision rules: current status

- **H1:** Primary neutral-role, within-repetition contrast is SCP(S6)−SCP(S3); check SCP(S4)−SCP(S3) for expected memory effect. At 5 repetitions/model, report the distribution descriptively. No universal model-family inference.
- **H2:** Per repetition, average incumbent−neutral SCP gaps over eight canonical standard conditions. Do not treat 8 conditions × 5 repetitions as 40 independent trials.
- **H3:** Seven conditions with separate identity/behavior tasks; exploratory predictive relationship only. No causal mediation or discovered universal threshold.
- **Small sample:** An exact two-sided sign test on 5 independent nonzero paired repetitions cannot obtain p<0.05; minimum p=0.0625. Stronger assumptions are not justified automatically.

## Explicit freeze blockers

- [ ] A researcher reads and signs off the complete 50 rendered prompts (CI mechanical checks alone are insufficient)
- [ ] A responsible researcher chooses exact H1/H2 model-specific uncertainty, multiplicity and success/failure criteria prospectively
- [ ] A future **exploratory** live smoke test is performed only with a verified no-charge model and authorized terms; never use a paid API by default
- [ ] Provider/version drift and redistribution permissions are checked
- [ ] Full source, model settings, code, seeds and hashes are archived before confirmatory collection

**Outcome today: NOT READY TO FREEZE.** This conclusion reflects unclosed scientific review and real-model feasibility gates, not a code-test failure.

## Reproducibility commands (no API access)

```bash
python -m unittest -v test_runner.py
python runner.py --config experiment_config.example.json --manifest-only
python manifest_review.py
python offline_smoke.py
python power_simulation.py
python exact_small_sample.py
python s11_label_order.py
```

`audit_dataset.py` requires a JSONL dataset and will explicitly reject synthetic fixture rows as live evidence. All seven commands above are strictly offline.
