# One Day — 18 November 2026

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/adzinsyariif/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/adzinsyariif/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

An entry for the make.fun bounty ["Sum up 18 November's world news in one image"](https://make.fun/bounty/news-image-20261118).

**One Day — 18 November 2026** is a single-image newspaper front page for Wednesday
18 November 2026. A watercolour hero shows Trump, Xi and Putin shaking hands at a
summit table in Shenzhen — US, Chinese and Russian flags behind them, the Shenzhen
skyline at dusk — under the headline of the first trilateral summit at APEC. Around it,
eight panels sum up the rest of the day: the Hormuz escalation, Ukraine's strike on the
Crimea Bridge, Israel's new Gaza operation, the US losing measles-free status, the tech
outage wave, NVIDIA's beat and Anthropic's $83 IPO on a mixed Wall Street, the Siberia
plane crash, and Cyclone Akvan nearing Odisha.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` (Node 22, standard library only, no network) creates the output directory if needed and copies the repository's
`entry.png` to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png`). It runs
deterministically: both runs write byte-identical output.

## Layout

- `main.ts` — the program: copies `entry.png` to the output path.
- `entry.png` — the finished 1024×1024 front page (JPEG bytes, 303,291 bytes).
- `compose.py` — the Python/PIL compositing script that built `entry.png` from the
  generated hero artwork: masthead, hero crop, headline band and the eight-panel grid.
- `LICENSE` — MIT.

## License

MIT — see `LICENSE`.
