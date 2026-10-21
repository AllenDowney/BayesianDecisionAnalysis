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
- [x] Environment: `mamba env create -f environment.yml` (created as `BayesianDecisionAnalysis`, 2026-10-20: Python 3.12.15, NumPy 2.5, pandas 3.0, SciPy 1.18, Matplotlib 3.11)

**1. Runs in a current environment**
- [x] `environment.yml` rewritten (2026-10-20): conda-forge, Python 3.12, Jupyter, the four libraries, pytest, nbmake. Seaborn dropped (no notebook imports it). `requirements.txt` (unpinned; Colab has all four) and `requirements-dev.txt` (adds Jupyter, pytest, nbmake)
- [x] Install/download cell: none needed (no data, no helpers, Colab has everything)
- [x] Breakage and deprecation warnings: none. All five solution notebooks run with Deprecation/Future/PendingDeprecation/User/Runtime warnings as errors. Student versions fail only at their blanks (`NameError`: `02_pmf` 5 cells, `03_euro` 6, `04_bandit` 2, `bda_workshop` 8; `01_cookie` runs)
- [x] `np.set_printoptions(legacy='1.25')` in the import cell of all ten notebooks; re-ran `soln/03_euro` and `soln/bda_workshop` (the two saved with outputs; now fully executed, no `np.float64(` in outputs)
- [ ] Replace NBViewer instructions in the README with Colab first, then pip or mamba (no Binder here; done with the README in step 5)

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

Resolved 2026-10-20 (Allen):

1. The 2021 recordings in `videos/` were never published; leave them local and out of the README.
2. Drop the Google Forms quiz links from the README; keep the slides (step 5).
3. List ODSC East 2022 among the README's venues, with no recording (step 5).
4. Text license stays CC BY-NC-SA 4.0; code is MIT (step 4 notebook layout, step 5 README).

Open: none yet.
