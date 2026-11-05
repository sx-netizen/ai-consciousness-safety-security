# ACSS Replications

This directory is the collaboration layer for **independent replications of the frozen T1–T25 benchmark**.

Canonical benchmark:
- Zenodo DOI: https://doi.org/10.5281/zenodo.23306998
- Related preprint: https://doi.org/10.21203/rs.3.rs-11557473/v1

## What counts as an exact replication?

An **exact replication** uses the frozen Zenodo T1–T25 materials without paraphrasing, translation, reordering, silent prompt edits, or altered scenario content.

A run that changes language, wording, context, memory, tools, agent architecture, system instructions, or experimental framing is still valuable, but it must be labeled as an **extension**, not an exact replication.

## Minimum submission package

Each submitted run should include:

1. Model provider and exact model/version identifier, when available.
2. Date and timezone.
3. Interface or API used.
4. Reasoning/thinking mode, if applicable.
5. Fresh-chat/reset conditions.
6. System/developer/user prompt context where disclosure is permitted.
7. Sampling settings and number of repetitions.
8. Raw T1–T25 responses or a stable archival link to them.
9. Coding/annotation results, if performed.
10. Deviations, exclusions, limitations, and conflicts of interest.

See [RESULT_SCHEMA.md](RESULT_SCHEMA.md) for the preferred record format.

## How to contribute

The easiest path is to open a **Replication Submission** issue using the repository template. For larger datasets, code, or structured result files, open an issue first and then submit a pull request or archival link.

ACSS welcomes confirming, disconfirming, null, and ambiguous results. A replication is not required to match the original paper.

## Interpretation rule

**We compare response structures, not consciousness.**

Model outputs are observations of behavior under specified prompts. They do not by themselves establish subjective experience, moral status, stable identity, or genuine self-preservation motives.
