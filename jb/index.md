---
myst:
  html_meta:
    description: "A hands-on Python tutorial on Bayesian decision analysis: Bayes's theorem, estimating proportions, and Thompson sampling for the Bayesian bandit."
og:description: "A hands-on Python tutorial on Bayesian decision analysis: Bayes's theorem, estimating proportions, and Thompson sampling for the Bayesian bandit."
---

# Bayesian Decision Analysis: A Tutorial in Python

[Allen Downey](https://allendowney.com)

This is self-study material: the workshop is not offered live now, but the notebooks are maintained and run on Colab. For a newer version that uses PyMC, see [Bayesian Decision Analysis with PyMC](https://allendowney.github.io/BDAwithPyMC/).

This tutorial is a hands-on introduction to Bayesian Decision Analysis (BDA), which is a framework for using probability to guide decision-making under uncertainty. I start with Bayes's Theorem, which is the foundation of Bayesian statistics, and work toward the Bayesian bandit strategy, which is used for A/B testing, medical tests, and related applications. In addition to the bandit strategy, the slides summarize two other applications of BDA, optimal bidding and deriving a decision rule.

The examples in this tutorial are from my book, [*Think Bayes*](https://allendowney.github.io/ThinkBayes2/).

**Level:** introductory. You should be familiar with Python at an intermediate level, and with Jupyter notebooks. We'll use NumPy, SciPy, and pandas, but I'll explain what you need to know as we go. You should be familiar with basic probability, but you don't need to know anything about Bayesian statistics.

**Length:** about 90 minutes.

## The notebook

The page on this site shows the notebook with solutions. To do the exercises, run the version with blanks on Colab:

* [From Bayes's Theorem to Bayesian Bandits](bda_workshop): the five urn problem, Bayesian updates with a pandas `Series`, and the Bayesian bandit with Thompson sampling. [Exercises on Colab](https://colab.research.google.com/github/AllenDowney/BayesianDecisionAnalysis/blob/main/bda_workshop.ipynb)

[Slides for this tutorial are here](https://docs.google.com/presentation/d/e/2PACX-1vTP6Xwls3yF9osvXG78tiH8vvaBHXDtUDHvQiGhVtUrgFflWWyBgqbkqRy9cDTCxS1nxnI5P09TPDxY/pub).

## Extended version

An earlier, longer version of the workshop covers the same material in four notebooks. They run on Colab; each link opens the version with blanks, which links to the solutions.

1. [Bayes's Theorem](https://colab.research.google.com/github/AllenDowney/BayesianDecisionAnalysis/blob/main/01_cookie.ipynb): the cookie problem and Bayes tables.
2. [Distributions](https://colab.research.google.com/github/AllenDowney/BayesianDecisionAnalysis/blob/main/02_pmf.ipynb): the 101 Bowls problem and probability mass functions.
3. [Bayesian Statistics](https://colab.research.google.com/github/AllenDowney/BayesianDecisionAnalysis/blob/main/03_euro.ipynb): the Euro problem, priors, and credible intervals.
4. [Bayesian Bandits](https://colab.research.google.com/github/AllenDowney/BayesianDecisionAnalysis/blob/main/04_bandit.ipynb): Thompson sampling.

[Slides for the extended version are here](https://docs.google.com/presentation/d/e/2PACX-1vSqEEhwzKyzIRGORZpEuU-a0iFyePxslNBhRB6f-3wFVQjZlj119EXlAOTFz02WQzh1oYFYjG1-RWIf/pub).

## Recordings

I presented this tutorial at ODSC East 2022 and PyData Global 2022. The recording is from [PyData Global 2022](https://www.youtube.com/watch?v=fsdbneHgi58&t=228). The code in the video is an earlier version; the [repository README](https://github.com/AllenDowney/BayesianDecisionAnalysis) lists the version that goes with it.

## Next steps

For a newer version of this workshop that uses PyMC, see [Bayesian Decision Analysis with PyMC](https://allendowney.github.io/BDAwithPyMC/). To go further, read [*Think Bayes*](https://allendowney.github.io/ThinkBayes2/), which is free online, or see [my other workshops](https://allendowney.github.io/#workshops).

The code is on [GitHub](https://github.com/AllenDowney/BayesianDecisionAnalysis), under the MIT License; the text is under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
