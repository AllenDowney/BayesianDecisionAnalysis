# BayesianDecisionAnalysis Project Board

Numbered tasks for tracking work. Each task has a permanent number; add new tasks at the end. Update status as work progresses.

**Status values:** `Pending`, `In progress`, `DONE`

---

## Task 1: Refresh

**Status:** DONE (2026-10-21)

**Context:** BayesianDecisionAnalysis is a **self-study** workshop (GreenTeaPress Task 24): not offered live now, but the notebooks are maintained and run on Colab. BDAwithPyMC is the newer take; the README points to it. Guide: the "Refresh checklist" (self-study variant) in `~/GreenTeaPress/plans/workshops.md`; BayesMadeSimple and CompStats are worked examples. 78 stars. Given at ODSC East 2022 and PyData Global 2022; the recording is [PyData Global 2022](https://www.youtube.com/watch?v=fsdbneHgi58).

**0. Set up**
- [x] `git fetch`/pull (7 README commits behind, fast-forwarded); uncommitted edits and untracked files decided (below)
- [x] `PROJECT_BOARD.md` and `CLAUDE.md` (2026-10-20)
- [x] Tags (pushed 2026-10-20): `pydata-global-2022` at `74fee29` (2022-11-29, the last commit before the conference, Dec 1–3; the next commits are README edits on 12-04); `pre-refresh-2026` at `2c84da0`. ODSC East 2022 was not recorded, so no tag
- [ ] README: each recording lists its tag
- [x] Inventory (below)
- [x] Environment: `mamba env create -f environment.yml` (created as `BayesianDecisionAnalysis`, 2026-10-20; recreated on Python 3.13.16 on 2026-10-21: NumPy 2.5, pandas 3.0, SciPy 1.18, Matplotlib 3.11)

**1. Runs in a current environment**
- [x] `environment.yml` rewritten (2026-10-20): conda-forge, Python 3.13 (Colab's since 2026-08-19; moved from 3.12 on 2026-10-21 after the checklist changed, and the solutions re-checked with warnings as errors), Jupyter, the four libraries, pytest, nbmake. Seaborn dropped (no notebook imports it). `requirements.txt` (unpinned; Colab has all four) and `requirements-dev.txt` (adds Jupyter, pytest, nbmake)
- [x] Install/download cell: none needed (no data, no helpers, Colab has everything)
- [x] Breakage and deprecation warnings: none. All five solution notebooks run with Deprecation/Future/PendingDeprecation/User/Runtime warnings as errors. Student versions fail only at their blanks (`NameError`: `02_pmf` 5 cells, `03_euro` 6, `04_bandit` 2, `bda_workshop` 8; `01_cookie` runs)
- [x] `np.set_printoptions(legacy='1.25')` in the import cell of all ten notebooks; re-ran `soln/03_euro` and `soln/bda_workshop` (the two saved with outputs; now fully executed, no `np.float64(` in outputs)
- [ ] Replace NBViewer instructions in the README with Colab first, then pip or mamba (no Binder here; done with the README in step 5)

**2. Tests and CI**
- [x] `pytest --nbmake soln/*.ipynb`: the five solutions pass (about 15 s). Student versions not tested (Allen, 2026-10-20): they stop at their blanks, and no `raises-exception` tags
- [x] `.github/workflows/tests.yml` (push to `main`, PR, monthly, manual; Python 3.13 (3.12 until 2026-10-21); pip with `requirements-dev.txt`; 20-minute timeout; `actions/checkout@v5`, `actions/setup-python@v6`); badge at the top of the README. First run passed in 39 s (2026-10-20, run 39521304861). Annotation: `ubuntu-latest` moves to Ubuntu 26 from 2026-10-19 (informational)

**3. Colab**
- [x] "Click here to run this notebook on Colab" cell after the title of all ten notebooks; solutions also link to the version with blanks (2026-10-20). README table: step 5
- [x] Build scripts: `remove_soln.py` now points the Colab cell at the student version; root `build.sh` passed no filenames to `remove_soln.py` (so it did nothing), now `0*.ipynb`. A scratch rebuild from `soln/` reproduces the committed student versions of `01`–`04` exactly (after carrying "wining" → "winning" into the student `04_bandit`). `bda_workshop` is outside `build.sh`; keep it in sync by hand
- [x] Allen ran `soln/bda_workshop` on Colab end to end (2026-10-21)

**4. Text**
- [x] Typos and docstrings (2026-10-20, student and solution versions): "divide-and conquer", "the the" (2), a missing period, "probide", "Having see", "Aposteori"/"aposteori" → "A Posteriori"/"a posteriori", "probabily", "prior believe", "proability", "If use", "each distributions", "Chose a machine", "an end itself", `num_play` → `num_plays`, "decisions theory", "9 loss" → "9 losses"; 02_pmf exercise "bowls 51 through 101" → "100" (bowls go 0–100) and its solution plot title 'One cookie' → 'Three draws'; `credible_interval` docstring said "Compute the mean of a PMF"; `update` docstring said "Likelihood function for Bayesian bandit"
- [x] Links: MacKay http → https; LessWrong wiki link → `lesswrong.com/w/bayesian-decision-theory` (as in BayesMadeSimple); the rest return 200
- [x] Notebook layout: H1 title plus one-line subtitle ("Examples and exercises for the tutorial [Bayesian Decision Analysis](…)", as in CompStats), Colab cell, `##` sections; copyright ("2021–2026"; `bda_workshop` "2022–2026") and licenses (code MIT, text CC BY-NC-SA 4.0) in a cell at the end; the old trailing empty cell dropped. Rebuilding 01–04 with `build.sh` still reproduces the student versions; `bda_workshop` versions aligned cell for cell (its student blanks are `fill-in` cells)
- [x] Everything else under "Content issues"

**5. README in the standard shape**
- [x] README rewritten (2026-10-21): title, badge, author, self-study line with BDAwithPyMC, abstract, *Think Bayes* (2e site), hub link, level (introductory; intermediate Python), length (about 90 minutes, Allen), outline, workshop table and extended-version table with Colab links, both slide decks, recordings (ODSC East 2022; PyData Global 2022 with tag `pydata-global-2022`), running instructions (Colab, pip, mamba), next steps, license (code MIT, text CC BY-NC-SA 4.0). Quiz and NBViewer links dropped. All links return 200
- [x] README: each recording lists its tag (step 0 item)

**6. Site and visibility** (self-study: no new site by default; Allen chose a small notebook site, 2026-10-21)
- [x] Site is the README via Jekyll (Pages: `main` /). `_config.yml` (2026-10-21): title, description (Allen approved), `url`/`baseurl`, `jekyll-sitemap`, `jekyll-seo-tag`, Think Bayes cover as social image, `exclude:` so the README is the only page. Page-view counter in `_includes/head-custom.html`
- [x] Checked live: title "Bayesian Decision Analysis | <description>", one `name="description"`, `og:description`, `og:image`, `rel="canonical"`, counter script; `sitemap.xml` lists only the landing page; `PROJECT_BOARD.html` and `CLAUDE.html` now 404 (they were public from 2026-10-20 until this change)
- [x] `Sitemap:` line in `~/AllenDowney.github.io/robots.txt` (pushed, `9bad4f6`)
- [x] Allen submitted the sitemap in Search Console (2026-10-21); ticked in GreenTeaPress Task 22
- [x] Notebook site (Allen, 2026-10-21; replaces the Jekyll README site above): `jb/` from the BayesMadeSimple template, a landing page (`index.md`) and `bda_workshop` only (page title "From Bayes's Theorem to Bayesian Bandits", since the notebook's H1 is the site title); the extended version is linked on Colab. Descriptions approved by Allen. Test build in scratch: sitemap lists the two pages; each has one description, `og:description`, canonical, the Think Bayes cover and the counter. Published with `./build.sh publish`; Pages switched from `main` / to `gh-pages`; root `_config.yml` and `_includes/` removed. Sitemap URL unchanged, so `robots.txt` and Search Console need nothing new
- [x] Repo description (Allen approved) and topic `thompson-sampling` set with `gh`; `scripts/repo_about.sh` entry updated (GreenTeaPress, uncommitted). Hub entry still accurate, no change

**7. Close**
- [x] Tag `2026-refresh` (2026-10-21); note in GreenTeaPress Task 24

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

Open (from the step 4 read-through, 2026-10-20):

5. `02_pmf`, "Summarizing the posterior": "The posterior distribution has a peak near 60%" and two lines later "The peak … is at 67%".
6. `03_euro`, batting-average exercise solution: `likelihood_hit = xs / 100`, but here `xs` are batting averages (0 to 0.5), so it should be `xs`. The answer is the same (the factor cancels when normalizing), but it's misleading.
7. `03_euro` says "`Pmf`" / "takes a Pmf" where the code uses a `Series` (BayesMadeSimple reworded the same text).
8. `04_bandit`: the sentence before `pmf_choice` describes `choose` (it "chooses among the machines … proportional to its probability of superiority"); `bda_workshop` says "equal to", which is right.
9. `bda_workshop`: after `update`, "It uses the quantities in the index to compute the likelihood" no longer matches the code, which uses the global `likelihood_win` and `likelihood_loss`.
10. `bda_workshop` and `04_bandit`: exercises are numbered "Exercise 3" and "Exercise 4" with no 1 and 2 (leftovers from the longer version).
11. `bda_workshop`: "The results are the same as what we worked through in the slides" (fine with the slides; odd for self-study).
