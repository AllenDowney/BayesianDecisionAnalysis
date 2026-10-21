# Bayesian Decision Analysis

[![tests](https://github.com/AllenDowney/BayesianDecisionAnalysis/actions/workflows/tests.yml/badge.svg)](https://github.com/AllenDowney/BayesianDecisionAnalysis/actions/workflows/tests.yml)

[Allen Downey](https://allendowney.com)

This is self-study material: the workshop is not offered live now, but the notebooks are maintained and run on Colab. For a newer version that uses PyMC, see [Bayesian Decision Analysis with PyMC](https://github.com/AllenDowney/BDAwithPyMC).

This tutorial is a hands-on introduction to Bayesian Decision Analysis (BDA), which is a framework for using probability to guide decision-making under uncertainty. I start with Bayes's Theorem, which is the foundation of Bayesian statistics, and work toward the Bayesian bandit strategy, which is used for A/B testing, medical tests, and related applications. For each step, I provide a Jupyter notebook where you can run Python code and work on exercises. In addition to the bandit strategy, I summarize two other applications of BDA, optimal bidding and deriving a decision rule. Finally, I suggest resources you can use to learn more.

The examples in this tutorial are from my book, [*Think Bayes*](https://allendowney.github.io/ThinkBayes2/).

This is one of [my workshops and tutorials](https://allendowney.github.io/#workshops).

**Level:** introductory. You should be familiar with Python at an intermediate level, and with Jupyter notebooks. We'll use NumPy, SciPy, and pandas, but I'll explain what you need to know as we go. You should be familiar with basic probability, but you don't need to know anything about Bayesian statistics.

**Length:** about 90 minutes.

## Outline

* Problem statement: A/B testing, medical tests, and the Bayesian bandit problem
* Prerequisites and goals
* Bayes's theorem and the five urn problem
* Using pandas to represent a PMF
* Estimating proportions
* From belief to strategy
* Implementing and testing Thompson sampling
* More generally: two other examples of BDA
* Resources and next steps

The workshop notebook comes in two versions: one with blanks for the exercises, and one with solutions.

| Notebook | Exercises | Solutions |
|---|---|---|
| Bayesian Decision Analysis | [Run on Colab](https://colab.research.google.com/github/AllenDowney/BayesianDecisionAnalysis/blob/main/bda_workshop.ipynb) | [Run on Colab](https://colab.research.google.com/github/AllenDowney/BayesianDecisionAnalysis/blob/main/soln/bda_workshop.ipynb) |

[Slides for this tutorial are here](https://docs.google.com/presentation/d/e/2PACX-1vTP6Xwls3yF9osvXG78tiH8vvaBHXDtUDHvQiGhVtUrgFflWWyBgqbkqRy9cDTCxS1nxnI5P09TPDxY/pub).

### Extended version

An earlier, longer version of the workshop covers the same material in four notebooks, starting with the cookie problem and the Euro problem. [Slides for the extended version are here](https://docs.google.com/presentation/d/e/2PACX-1vSqEEhwzKyzIRGORZpEuU-a0iFyePxslNBhRB6f-3wFVQjZlj119EXlAOTFz02WQzh1oYFYjG1-RWIf/pub).

| Notebook | Exercises | Solutions |
|---|---|---|
| 1. Bayes's Theorem | [Run on Colab](https://colab.research.google.com/github/AllenDowney/BayesianDecisionAnalysis/blob/main/01_cookie.ipynb) | [Run on Colab](https://colab.research.google.com/github/AllenDowney/BayesianDecisionAnalysis/blob/main/soln/01_cookie.ipynb) |
| 2. Distributions | [Run on Colab](https://colab.research.google.com/github/AllenDowney/BayesianDecisionAnalysis/blob/main/02_pmf.ipynb) | [Run on Colab](https://colab.research.google.com/github/AllenDowney/BayesianDecisionAnalysis/blob/main/soln/02_pmf.ipynb) |
| 3. Bayesian Statistics | [Run on Colab](https://colab.research.google.com/github/AllenDowney/BayesianDecisionAnalysis/blob/main/03_euro.ipynb) | [Run on Colab](https://colab.research.google.com/github/AllenDowney/BayesianDecisionAnalysis/blob/main/soln/03_euro.ipynb) |
| 4. Bayesian Bandits | [Run on Colab](https://colab.research.google.com/github/AllenDowney/BayesianDecisionAnalysis/blob/main/04_bandit.ipynb) | [Run on Colab](https://colab.research.google.com/github/AllenDowney/BayesianDecisionAnalysis/blob/main/soln/04_bandit.ipynb) |

## Recordings

I presented this tutorial at ODSC East 2022 and PyData Global 2022. The code in the video is not the current version; the tag after the link is the version of the code that goes with it.

* [PyData Global 2022](https://www.youtube.com/watch?v=fsdbneHgi58&t=228): tag [`pydata-global-2022`](https://github.com/AllenDowney/BayesianDecisionAnalysis/tree/pydata-global-2022)

## Running the notebooks

The easiest way to run the notebooks is on Colab: click one of the links above. You need a Google account, but you don't have to install anything.

To run them on your own computer, you need Python 3 with Jupyter, NumPy, pandas, SciPy, and Matplotlib. You can [download the code in this zip file](https://github.com/AllenDowney/BayesianDecisionAnalysis/archive/main.zip), or clone the repository:

```
git clone https://github.com/AllenDowney/BayesianDecisionAnalysis
cd BayesianDecisionAnalysis
```

Then install the packages with pip:

```
pip install -r requirements.txt
```

Or, if you use conda or mamba, create an environment:

```
mamba env create -f environment.yml
mamba activate BayesianDecisionAnalysis
```

Then run `jupyter lab` and open `bda_workshop.ipynb`.

## Next steps

For a newer version of this workshop that uses PyMC, see [Bayesian Decision Analysis with PyMC](https://github.com/AllenDowney/BDAwithPyMC). To go further, read [*Think Bayes*](https://allendowney.github.io/ThinkBayes2/), which is free online, or see [my other workshops](https://allendowney.github.io/#workshops).

## License

The code is available under the [MIT License](LICENSE). The text is available under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).
