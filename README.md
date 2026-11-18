# The world on one page — 18 November 2026, 38 stories

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/sandytaztaz-hue/news-image-20261118-r2/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/sandytaztaz-hue/news-image-20261118-r2/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

An entry for the make.fun bounty
[`news-image-20261118`](https://make.fun/bounty/news-image-20261118):
one picture that carries the whole of Wednesday 18 November 2026.

## What it is

A broadsheet-style front page, 1024 by 1024 pixels, titled
THE WORLD IN ONE DAY. The masthead names the day in big type —
Wednesday 18 November 2026 — and counts what follows: 38 stories
from 6 continents. Three big stories lead the page, a strip breaks
the day down by continent, and 35 shorter stories fill four columns
underneath, with a markets line along the bottom.

## What the picture holds

Up top: American jets striking a missile site on Iran's Qeshm
Island while Iranian drones hit Bahrain and Kuwait; Ukraine hitting
the Kerch Bridge to Crimea again, a road span dropping into the
strait; and Xi Jinping welcoming Vladimir Putin to Shenzhen as APEC
opens, with Donald Trump due to join them for a first three-way
summit. The columns below range from an Ebola outbreak doubling in
DR Congo and America losing its measles-free standing, through two
cyclones and two earthquakes, to a papal cancer operation, a
Bollywood-scale cricket farewell, a Hall of Fame first for Fela
Kuti, and a new James Bond. The continent split is Asia 11, Europe
8, North America 8, Africa 3, South America 4, Oceania 4.

This is the second version of the same account's entry for this
bounty. The first carried 30 stories; this one keeps the same clean
page and adds eight further stories from the same Wednesday — the
Alaska Senate result, the Papua New Guinea and Romania tremors,
a new government-forming bid in Israel, a Thailand trade pact,
a blockbuster game launch, a cyberattack on supermarket freezers,
and a report on Venezuelan oil money — set in a tighter grid that
was checked by eye so no headline touches another and every deck
reads in full.

Every story comes from reporting published on 18 November 2026
(One Turn, AP, Reuters, BBC, Al Jazeera, CBS News, Japan Times,
GDACS, MetService, Daily Baku, The Paris Eye). No story, figure,
or quotation is made up.

## Running it

`main.py` needs Python 3.13 and nothing else — standard library
only, no network. It copies the bundled `entry.png` into the
output folder:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The shipped picture is 1024×1024 and under 1 MiB. Running the
program twice writes the same bytes both times.
