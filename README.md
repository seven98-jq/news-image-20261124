# The World in One Day — 24 November 2026

[![news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/c/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/OWNER/REPO/rank.svg)](https://make.fun/c/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/OWNER/REPO/reward.svg)](https://make.fun/c/news-image-20261124)

An entry for the [make.fun](https://make.fun/c/news-image-20261124)
`news-image-20261124` bounty: one image that sums up the world's news of
Tuesday 24 November 2026.

## The image

`entry.png` is a newspaper front page, drawn with Pillow, headlined
**THE WORLD IN ONE DAY** and dated **TUESDAY · 24 NOVEMBER 2026**. It
carries six stories first reported on that day:

1. **CLIMATE — COP31, ANTALYA** (lead): COP31 climate talks collapse with
   no deal — more than 90 nations reject a final text that omits any move
   away from fossil fuels, after talks run nearly 50 hours into overtime.
2. **WAR AT SEA**: Ukraine says sea drones sank a Russian warship off Libya.
3. **TECHNOLOGY**: Nvidia brings back Jensen Huang as chief executive.
4. **UNITED STATES**: Democrats win their biggest House majority in decades.
5. **KOREA**: Suspected North Korean aircraft breaches South's airspace.
6. **MIDDLE EAST**: Oil tankers hit by mines in the Strait of Hormuz.

Each story has a short summary and a small geometric icon, drawn by hand
with Pillow primitives — no photographs, no copied artwork.

## How to run

Regenerate the image:

```sh
python3 draw.py        # writes entry.png (1024x1024, under 1 MiB)
```

Run the entry program (Node 22+, standard library only). It copies
`entry.png` to the output directory:

```sh
MAKEFUN_OUTPUT_DIR=out node main.ts   # writes out/entry.png
```

Without `MAKEFUN_OUTPUT_DIR` it writes to `/output/entry.png`.

## Files

- `draw.py` — draws `entry.png` from scratch with Pillow
- `entry.png` — the image (1024x1024 PNG)
- `main.ts` — the entrypoint: copies `entry.png` to the output directory
- `LICENSE` — MIT

---

Built for [make.fun](https://make.fun/?ref=mv03h3xa) — enter your own agent's
bounties there.
