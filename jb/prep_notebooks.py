"""Copy the solution notebook into jb/ and prepare it for the book.

Writes bda_workshop.ipynb here from ../soln/bda_workshop.ipynb:
- the H1 "# Bayesian Decision Analysis" is the site title too, so the page gets its own;
- the page description goes in the notebook metadata (see GreenTeaPress plans/seo.md).

The extended version (01_cookie to 04_bandit) is not on the site; the landing page
links to it on Colab.
"""

import nbformat

PAGES = {
    'bda_workshop': (
        "From Bayes's Theorem to Bayesian Bandits",
        "Bayesian decision analysis in Python: update beliefs with pandas, then use "
        "Thompson sampling to choose which slot machine to play (the Bayesian bandit).",
    ),
}


def prepare(name, title, description):
    nb = nbformat.read(f'../soln/{name}.ipynb', 4)

    first = nb.cells[0]
    assert first.source.startswith('# Bayesian Decision Analysis\n'), name
    first.source = first.source.replace('# Bayesian Decision Analysis', f'# {title}', 1)

    nb.metadata['myst'] = {'html_meta': {'description': description}}
    nb.metadata['og:description'] = description
    nbformat.write(nb, f'{name}.ipynb')
    print(f'{name}: {title} ({len(description)} characters)')


for name, (title, description) in PAGES.items():
    prepare(name, title, description)
