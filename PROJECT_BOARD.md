# BayesianDecisionAnalysis Project Board

Numbered tasks for tracking work. Each task has a permanent number; add new tasks at the end. Update status as work progresses.

**Status values:** `Pending`, `In progress`, `DONE`

---

## Task 1: Refresh

**Status:** In progress (2026-10-20)

**Context:** BayesianDecisionAnalysis is a **self-study** workshop (GreenTeaPress Task 24): not offered live now, but the notebooks are maintained and run on Colab. BDAwithPyMC is the newer take; the README points to it. Guide: the "Refresh checklist" (self-study variant) in `~/GreenTeaPress/plans/workshops.md`; BayesMadeSimple and CompStats are worked examples. 78 stars. Given at ODSC East 2022 and PyData Global 2022; the recording is [PyData Global 2022](https://www.youtube.com/watch?v=fsdbneHgi58).

**0. Set up**
- [x] `git fetch`/pull (7 README commits behind, fast-forwarded); uncommitted edits and untracked files decided (below)
- [x] `PROJECT_BOARD.md` and `CLAUDE.md` (2026-10-20)
- [x] Tags (pushed 2026-10-20): `pydata-global-2022` at `74fee29` (2022-11-29, the last commit before the conference, Dec 1–3; the next commits are README edits on 12-04); `pre-refresh-2026` at `2c84da0`. ODSC East 2022 was not recorded, so no tag
- [ ] README: each recording lists its tag
- [x] Inventory (below)
- [ ] Environment: `mamba env create -f environment.yml` (name `BayesianDecisionAnalysis`), after `environment.yml` is rewritten in step 1

**1. Runs in a current environment**
- [ ] `environment.yml` (conda-forge, Python 3.12, pytest, nbmake), `requirements.txt`, `requirements-dev.txt`
- [ ] Install/download cell if needed (probably none: Colab has all five libraries; no data, no helpers)
- [ ] Breakage and deprecation warnings (run scratch copies with warnings as errors)
- [ ] `np.set_printoptions(legacy='1.25')` in the cell that imports NumPy; re-run notebooks saved with outputs
- [ ] Replace NBViewer/Binder-era instructions with Colab first, then pip or mamba

**2. Tests and CI**
- [ ] `pytest --nbmake` on the solutions (and the student versions if they run)
- [ ] `.github/workflows/tests.yml` (push to `main`, PR, monthly, manual; Python 3.12; `actions/checkout@v5`, `actions/setup-python@v6`); badge in the README

**3. Colab**
- [ ] "Click here to run this notebook on Colab" cell after the title of each notebook (solutions also link to the version with blanks); Colab links in the README table
- [ ] Allen runs one notebook on Colab end to end

**4. Text**
- [ ] Clear typos, wrong docstrings, broken links (codespell; read the markdown)
- [ ] Notebook layout: one `#` H1 title, at most a one-line subtitle, Colab cell, `##` sections; copyright ("Copyright 2021–2026 Allen Downey") and license (code MIT, text CC BY-NC-SA 4.0?) in a markdown cell at the end. Student and solution versions alike
- [ ] Everything else under "Content issues"

**5. README in the standard shape**
- [ ] Self-study line at the top; title, badge, author, abstract, level, length, outline, notebook table, slides, recordings with tags, running instructions, next steps (BDAwithPyMC, *Think Bayes*, hub), license

**6. Site and visibility** (self-study: no new site)
- [ ] Existing site is the README via Jekyll (Pages: `main` /, root `_config.yml`); rebuild and do the `plans/seo.md` checklist on it
- [ ] Hub entry, repo description and topics

**7. Close**
- [ ] Tag `2026-refresh`; note in GreenTeaPress Task 24

### Inventory (2026-10-20)

Solutions are in `soln/` under the same names (not `_soln`). `soln/build.sh` runs nbmake on the solutions; the root `build.sh` copies `soln/0*.ipynb` up and runs `remove_soln.py` (clears outputs and `fill-in` cells, blanks cells that start with `# Solution`) to make the student versions.

**The workshop (PyData Global 2022), one notebook:**

| Notebook | Topic |
|---|---|
| `bda_workshop.ipynb` / `soln/bda_workshop.ipynb` | Bayes's theorem, PMFs, Euro problem, Bayesian bandit and Thompson sampling |

**Extended version (2021), four notebooks, kept on `main`:**

| Notebook | Topic |
|---|---|
| `01_cookie` | Bayes's theorem, cookie problem, Bayes tables |
| `02_pmf` | PMFs with pandas |
| `03_euro` | Euro problem |
| `04_bandit` | Bayesian bandit |

The README links a Google Forms quiz for each, and the extended slides.

All notebooks use NumPy, pandas, SciPy (`interpolate`, `stats`), Matplotlib and Seaborn; no data files, no helper modules. Notebook license: CC BY-NC-SA 4.0; `LICENSE` (MIT) covers the code.

**Removed from `main` (2026-10-20; in the tags and history):** `brisbane.ipynb`, from a June 2021 talk, "Bayesian Methods for Better Decision Making".

**Local state not in git (decided 2026-10-20):**

- Uncommitted solution edits in `soln/01`–`04` (2021: `make_bayes_table` in the cookie trick-coin exercise, a missing `# Solution` marker in `02_pmf`, `pmf.values` in `03_euro`, "wining" → "winning"): committed (`fe0d87d`); the committed student versions had been built from them. Kernel-metadata-only changes discarded.
- `build.sh`, `soln/build.sh`, `remove_soln.py`: committed. `cat_notebook.py`, `04_bandit-Copy1.ipynb` (identical to `04_bandit`), checkpoints: deleted (backed up in the session scratchpad).
- `videos/`: six mp4s from 2021-04-28 (705 MB, an edited recording of the extended version); kept locally, in `.gitignore`.

### Content issues

(For Allen to decide.)

1. Recordings in `videos/` (2021): published anywhere? If so, link them from the README.
2. The Google Forms quizzes and the two slide decks: still live and still matching the notebooks?
3. ODSC East 2022: add to the README's venues (no recording).
4. Text license: notebooks say CC BY-NC-SA 4.0; keep that (as in BiteSizeBayes) or another CC license?
