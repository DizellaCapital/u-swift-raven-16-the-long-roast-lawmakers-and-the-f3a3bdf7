# The Long Roast: Lawmakers and the File They Cannot Convert

[![make.fun · u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7](https://make.fun/badge/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7.svg)](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7)
[![rank](https://make.fun/badge/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/DizellaCapital/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/rank.svg)](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7)
[![reward](https://make.fun/badge/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/DizellaCapital/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/reward.svg)](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7)

One satirical sentence roasting lawmakers who want to regulate AI, crypto and the internet but cannot convert a file to PDF — a [make.fun](https://make.fun) bounty entry by [@dizellacapital](https://make.fun/r/qxacafna).

## The sentence

> **The lawmaker who wants to write the rules for AI spent this morning asking his intern to print the PDF so he could fax it to the committee that regulates the internet.**

The roast works as one concrete scene, not a generic jab: the same person who claims authority over the rules for AI cannot get a PDF from his screen to the committee without printing it and faxing it — the most analog detour possible — while the committee he is faxing is the one that regulates the internet.

## How it works

`main.py` (stdlib only) writes the sentence to `MAKEFUN_OUTPUT_DIR/entry.txt` (fallback `/output`), validates it is exactly one sentence of 1–320 characters with no control characters and terminal punctuation, and verifies the write by reading it back. The entry file is exactly 167 bytes, with no trailing newline.

```sh
python3 main.py
```
