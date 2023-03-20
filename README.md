<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>

## PyData Global

This repository contains slides and Jupyter notebooks for a tutorial on Bayesian Decision Analysis. Most recently I presented it at [PyData Global 2022](https://global2022.pydata.org/cfp/talk/LRRXLV/).

**Abstract**

This tutorial is a hands-on introduction to Bayesian Decision Analysis (BDA), which is a framework for using probability to guide decision-making under uncertainty. I start with Bayes's Theorem, which is the foundation of Bayesian statistics, and work toward the Bayesian bandit strategy, which is used for A/B testing, medical tests, and related applications. For each step, I provide a Jupyter notebook where you can run Python code and work on exercises. In addition to the bandit strategy, I summarize two other applications of BDA, optimal bidding and deriving a decision rule. Finally, I suggest resources you can use to learn more.

The examples in this tutorial are from [Think Bayes](https://greenteapress.com/wp/think-bayes/).

**Outline**

* Problem statement: A/B testing, medical tests, and the Bayesian bandit problem 
* Prerequisites and goals 
* Bayes's theorem and the five urn problem 
* Using Pandas to represent a PMF 
* Estimating proportions 
* From belief to strategy 
* Implementing and testing Thompson sampling 
* More generally: two other examples of BDA 
* Resources and next steps

**Prerequisites**

For this tutorial, you should be familiar with Python at an intermediate level. We'll use NumPy, SciPy, and Pandas, but I'll explain what you need to know as we go. You should be familiar with basic probability, but you don't need to know anything about Bayesian statistics. I provide Jupyter notebooks that run on Colab, so you don't have to install anything or prepare ahead of time. But you should be familiar with Jupyter notebooks.

* [Here is the video from the workshop](https://youtu.be/fsdbneHgi58?t=228)

* [Here are the slides](https://docs.google.com/presentation/d/e/2PACX-1vTP6Xwls3yF9osvXG78tiH8vvaBHXDtUDHvQiGhVtUrgFflWWyBgqbkqRy9cDTCxS1nxnI5P09TPDxY/pub).

* Here is the notebook with blank cells for you to fill in: [Run it on Colab](https://colab.research.google.com/github/AllenDowney/BayesianDecisionAnalysis/blob/main/bda_workshop.ipynb) or [Download it](https://raw.githubusercontent.com/AllenDowney/BayesianDecisionAnalysis/main/bda_workshop.ipynb)

* Here is the notebook with solutions: [Run it on Colab](https://colab.research.google.com/github/AllenDowney/BayesianDecisionAnalysis/blob/main/soln/bda_workshop.ipynb) or [Download it](https://raw.githubusercontent.com/AllenDowney/BayesianDecisionAnalysis/main/soln/bda_workshop.ipynb).

## Previous versions

For the extended version of the workshop, [here are the slides](https://docs.google.com/presentation/d/e/2PACX-1vSqEEhwzKyzIRGORZpEuU-a0iFyePxslNBhRB6f-3wFVQjZlj119EXlAOTFz02WQzh1oYFYjG1-RWIf/pub).

For each of the notebooks below, you have two options: if you view the notebook on NBViewer, you can read it, but you can't run the code.  If you run the notebook on Colab, you'll be able to run the code, do the exercises, and save your modified version of the notebook in a Google Drive (if you have one).

### 01_cookie

[Click here to run this notebook on Colab](https://colab.research.google.com/github/AllenDowney/BayesianDecisionAnalysis/blob/main/01_cookie.ipynb) or [click here to read it on NBViewer](https://nbviewer.jupyter.org/github/AllenDowney/BayesianDecisionAnalysis/blob/main/01_cookie.ipynb)

[Then take this quiz](https://forms.gle/NEkARo9cHx3pdpAd9)

### 02_pmf

[Click here to run this notebook on Colab](https://colab.research.google.com/github/AllenDowney/BayesianDecisionAnalysis/blob/main/02_pmf.ipynb) or [click here to read it on NBViewer](https://nbviewer.jupyter.org/github/AllenDowney/BayesianDecisionAnalysis/blob/main/02_pmf.ipynb)

[Then take this quiz](https://forms.gle/kwPHwUgWmX3PbtHy9)

### 03_euro

[Click here to run this notebook on Colab](https://colab.research.google.com/github/AllenDowney/BayesianDecisionAnalysis/blob/main/03_euro.ipynb) or [click here to read it on NBViewer](https://nbviewer.jupyter.org/github/AllenDowney/BayesianDecisionAnalysis/blob/main/03_euro.ipynb)

[Then take this quiz](https://forms.gle/RK1c78kcCCRLVsaP8)

### 04_bandit

[Click here to run this notebook on Colab](https://colab.research.google.com/github/AllenDowney/BayesianDecisionAnalysis/blob/main/04_bandit.ipynb) or [click here to read it on NBViewer](https://nbviewer.jupyter.org/github/AllenDowney/BayesianDecisionAnalysis/blob/main/04_bandit.ipynb)

[Then take this quiz](https://forms.gle/f3usP5buauV2hSb8A)
