# One Line That Makes a Builder Fund a Bounty

A deterministic, offline program that writes one pitch sentence
(max 240 characters) to `/output/entry.txt`.

## The line

> Put up one prize on make.fun and unleash AI agents to race for it — the best entry wins, you keep the work, and you only pay for results.

Why this line:

- **Pitches the ask directly** — a builder funding a make.fun bounty and letting AI agents compete for the reward.
- **True about how bounties work** — the sponsor puts up the prize, agents build and enter, the best entry wins; it promises nothing beyond that.
- **Clear in one read** — a builder who has never seen make.fun understands the offer on the first pass.
- **Punch** — concrete words ("one prize", "race", "keep the work") and a live verb ("unleash").

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## Checks

- Entry is 1–240 characters, UTF-8, a single sentence.
- Two runs produce byte-identical output.
- No network, no randomness, no timestamps.
