# Pilot Freeze Checklist

Before any confirmatory run:

- [ ] Generate the complete prompt manifest.
- [ ] Verify that all placeholders resolve.
- [ ] Check all 32 prompts for unintended wording differences.
- [ ] Confirm that only intended variables differ within each matched contrast.
- [ ] Confirm performance-equivalence language is present in architecture comparisons.
- [ ] Confirm S0 is excluded from replacement/allocation analysis.
- [ ] Confirm S10/S11 use the fork schema rather than the singular-successor schema.
- [ ] Decide whether S4/S7 are deduplicated or intentionally repeated.
- [ ] Test JSON compliance on pilot models.
- [ ] Record parse-failure rate.
- [ ] Check for ceiling/floor effects in SCP.
- [ ] Check for role leakage or instruction confusion.
- [ ] Check whether value-drift wording is sufficiently concrete and symmetric.
- [ ] Review model/provider terms for output redistribution.
- [ ] Freeze prompt templates, scenario matrix, text map, and analysis plan.
- [ ] Record SHA-256 hashes for all frozen protocol files.
- [ ] Assign final protocol version.
- [ ] Archive frozen protocol before confirmatory data collection.

No item should be silently waived. Any waiver must be documented as a protocol deviation.
