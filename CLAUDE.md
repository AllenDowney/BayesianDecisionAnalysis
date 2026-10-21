# BayesianDecisionAnalysis

Allen Downey's tutorial "Bayesian Decision Analysis": Bayes's theorem, PMFs with pandas, the Euro problem, and the Bayesian bandit (Thompson sampling), in Python. Given at ODSC East 2022 and PyData Global 2022. Self-study material now: not offered live, but the notebooks are maintained and run on Colab. The newer version is BDAwithPyMC. The GitHub Pages site (`allendowney.github.io/BayesianDecisionAnalysis/`) is the Jupyter Book in `jb/`, published to the `gh-pages` branch: a landing page and `bda_workshop` (the extended version is linked on Colab only).

**Guide for the 2026 refresh:** the "Refresh checklist" (self-study variant) in `~/GreenTeaPress/plans/workshops.md` (BayesMadeSimple and CompStats are worked examples). Progress goes on `PROJECT_BOARD.md` here (Task 1) and in GreenTeaPress Task 24.

## Which notebooks are the workshop

Student versions (with blanks) are at the top level; solutions are in `soln/` under the same names.

- `bda_workshop.ipynb`: the PyData Global 2022 workshop, one notebook.
- `01_cookie`, `02_pmf`, `03_euro`, `04_bandit`: the extended version (2021).

They need only NumPy, pandas, SciPy, Matplotlib and Seaborn; no data files and no helper modules.

Edit the solutions in `soln/`; the root `build.sh` copies `soln/0*.ipynb` up and runs `remove_soln.py` to make the student versions (cells tagged `fill-in` are emptied, cells starting with `# Solution` are blanked, outputs cleared). `bda_workshop.ipynb` is not covered by `build.sh`.

## Site

`jb/` builds the Jupyter Book site (`cd jb; ./build.sh [publish]`); `prep_notebooks.py` copies `soln/bda_workshop.ipynb` in, gives the page its own H1, and holds the page description. Template: BayesMadeSimple. Delete an old `jb/_build/` before publishing (`jb build` doesn't clean it).

## Tags

- `pydata-global-2022`: the code in the PyData Global 2022 video.
- `pre-refresh-2026`: the state before the 2026 refresh.

## Testing

Environment: `mamba env create -f environment.yml` (name `BayesianDecisionAnalysis`). Run the solutions top to bottom:

```
pytest --nbmake soln/*.ipynb
```

The target environment is Google Colab's current Python and libraries.

## Conventions

- Branch is `main`.
- Don't change the substance of the text; list content questions under "Content issues" on the board for Allen to decide.
- Keep student and solution versions in sync: same cells, solutions replaced by blanks.
- `videos/` holds local recordings and is ignored by git.
- Pages serves `gh-pages`, so committed `.md` files on `main` are not published.
