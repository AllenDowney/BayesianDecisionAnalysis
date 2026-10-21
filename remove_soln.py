import nbformat as nbf
import sys

# Collect a list of all notebooks in the content folder
filenames = sys.argv[1:]

text = '# Solution'
replacement = ''

colab_text = '[Click here to run this notebook on Colab]'
colab_url = 'https://colab.research.google.com/github/AllenDowney/BayesianDecisionAnalysis/blob/main/'

# Search through each notebook
for filename in filenames:
    ntbk = nbf.read(filename, nbf.NO_CONVERT)

    for cell in ntbk.cells:
        # point the Colab link at the version with blanks
        if cell['source'].startswith(colab_text):
            cell['source'] = f'{colab_text}({colab_url}{filename})'

        # remove tags
        if 'tags' in cell['metadata']:
            tags = cell['metadata']['tags']
            cell['metadata']['tags'] = []

            # Remove code from fill-in cells
            if 'fill-in' in tags:
                cell['source'] = ''

        # remove output
        if 'outputs' in cell:
            cell['outputs'] = []

        # remove solutions
        if cell['source'].startswith(text):
            cell['source'] = replacement

    nbf.write(ntbk, filename)
