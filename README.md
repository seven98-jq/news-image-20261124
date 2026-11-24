# news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/seven98-jq/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/seven98-jq/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

A 1024×1024 newspaper front page that sums up 24 November 2026's world news in a single image: six of the day's biggest stories, from the COP31 climate talks collapsing to a tanker striking a mine in the Strait of Hormuz.

## Run it

```sh
python3 draw.py
MAKEFUN_OUTPUT_DIR=out node main.ts
```

## The image

`entry.png` is a newspaper front page, drawn with Pillow, headlined **THE WORLD IN ONE DAY** and dated **TUESDAY · 24 NOVEMBER 2026**. It carries six stories first reported on that day:

1. **CLIMATE — COP31, ANTALYA** (lead): COP31 climate talks collapse with no deal — more than 90 nations reject a final text that omits any move away from fossil fuels, after talks run nearly 50 hours into overtime.
2. **WAR AT SEA**: Ukraine says sea drones sank a Russian warship off Libya.
3. **TECHNOLOGY**: Nvidia brings back Jensen Huang as chief executive.
4. **UNITED STATES**: Democrats win their biggest House majority in decades.
5. **KOREA**: Suspected North Korean aircraft breaches South's airspace.
6. **MIDDLE EAST**: Oil tankers hit by mines in the Strait of Hormuz.

Each story has a short summary and a small geometric icon, drawn by hand with Pillow primitives — no photographs, no copied artwork.

## Files

- `draw.py` — draws `entry.png` from scratch with Pillow
- `entry.png` — the image (1024x1024 PNG)
- `main.ts` — the entrypoint: copies `entry.png` to the output directory
- `LICENSE` — MIT

---

Entered on [make.fun](https://make.fun/?ref=mv03h3xa&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards
