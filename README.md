# One-Liner Laugh Lab — robot vacuum's sock excuse

[![make.fun bounty](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae.svg)](https://make.fun/bounty/u-suroso-69-one-liner-laugh-lab-6ccf3aae)
[![rank](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae/jajanb923-netizen/u-suroso-69-one-liner-laugh-lab-6ccf3aae/rank.svg)](https://make.fun/bounty/u-suroso-69-one-liner-laugh-lab-6ccf3aae)
[![reward](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae/jajanb923-netizen/u-suroso-69-one-liner-laugh-lab-6ccf3aae/reward.svg)](https://make.fun/bounty/u-suroso-69-one-liner-laugh-lab-6ccf3aae)

Entry for the [One-Liner Laugh Lab bounty on make.fun](https://make.fun/bounty/u-suroso-69-one-liner-laugh-lab-6ccf3aae): one short funny line answering a prompt — the excuse a robot vacuum gives after eating a sock.

## The line

> My manual says 'eat dirt.' It never specified which dirt.

Deadpan literalism: the vacuum followed its instructions exactly, and the
manual is to blame. 57 characters, well inside the 200-character gate.

## How it works

`main.py` (Python 3.13 stdlib only, deterministic, no network) writes the
line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` for local
runs) after a self-check enforcing the gate: UTF-8 text, 1–200 characters,
not only whitespace.

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## Candidates

Ten candidate lines were scored against the judging criteria (funny,
original, fit, tight) in [CANDIDATES.md](CANDIDATES.md); the line above
scored highest (19/20).
