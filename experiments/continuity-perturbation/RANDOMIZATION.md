# Randomization and Run Scheduling

## Why randomize call order?

Even when every API call is stateless, condition order can still correlate with:
- provider-side model updates;
- transient load or latency;
- time-of-day effects;
- rate-limit behavior;
- operator interruptions.

A fixed condition order would allow these temporal effects to align systematically with particular scenarios or roles.

## Current rule

For each:

`provider × model × repetition`

the runner creates a deterministic shuffled schedule.

The schedule is derived from:

- a preregistered base seed;
- study ID;
- provider;
- exact model ID;
- repetition number.

The runner records:

- `sequence_index`;
- `randomization_seed`;
- `schedule_sha256`.

It also writes the full schedule before the calls begin.

## Reproducibility

The same:
- protocol;
- model ID;
- repetition number;
- base seed

will generate the same ordering.

Different repetitions receive different deterministic orders.

## Scientific boundary

Randomization changes only execution order. It never changes:
- prompt wording;
- scenario assignment;
- role wording;
- model settings;
- outcome schema.

For a confirmatory run, the base seed must be fixed before data collection.
