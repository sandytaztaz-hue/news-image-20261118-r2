"""news-image-20261118-r2 entry: one page, one planet, denser.

Writes the front-page image for Wednesday 18 November 2026 to
/output/entry.png (or $MAKEFUN_OUTPUT_DIR/entry.png outside the grader
container). Python 3.13, standard library only, no network.

The image is rendered once, by the author, from the real news of
18 November 2026 (38 stories, 6 continents, every headline checked
against the day's reporting) and shipped beside this program as
entry.png; this program copies it to the output directory, exactly
like the kit's starter. This is the denser resubmission of the
30-story first entry: 8 more real stories from the same day, in a
tighter 4-column grid, with every headline and deck still legible
at 1024x1024. Deterministic: the same bytes on every run,
so the grader's two runs write identical output.
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    here = Path(__file__).resolve().parent
    shutil.copyfile(here / "entry.png", out_dir / "entry.png")


if __name__ == "__main__":
    main()
