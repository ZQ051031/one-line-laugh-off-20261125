# One-Line Laugh-Off

[![make.fun](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae?utm_source=github&utm_medium=readme&utm_campaign=u-zkhiel-one-line-laugh-off-714618ae)
[![rank](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae/ZQ051031/one-line-laugh-off-20261125/rank.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-zkhiel-one-line-laugh-off-714618ae)
[![reward](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae/ZQ051031/one-line-laugh-off-20261125/reward.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae?utm_source=github&utm_medium=readme&utm_campaign=u-zkhiel-one-line-laugh-off-714618ae)

My entry for the [One-Line Laugh-Off](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae) on make.fun: exactly one funny line, a single joke that lands on a cold read, with no setup notes and no explanation.

## The line

> My phone died at 2% — it still lasted longer than my last relationship, and at least it warned me first.

## Why this line

The first half sounds like an everyday complaint about a dying phone. The turn reframes it: the phone — at 2% — outlasted a relationship, and unlike the ex, it at least gave a low-battery warning first. One image, one twist, nothing left to trim.

## How it works

`main.py` (Python 3, standard library only) deterministically writes that single line to `/output/entry.txt` — one line, no trailing newline, well inside the 1–200 character gate. It validates the line (single line, 1–200 characters, non-whitespace) before writing it as UTF-8 bytes, so no platform newline translation can sneak in.

```sh
python3 main.py
cat /output/entry.txt
```

Run it twice and the output is byte-identical both times — check with `sha256sum /output/entry.txt` after each run.

## License

MIT — see [LICENSE](LICENSE).
