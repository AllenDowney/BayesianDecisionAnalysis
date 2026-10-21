
cp soln/0*.ipynb .

python remove_soln.py 0*.ipynb

git add 0*.ipynb
git commit -m "Updating the notebooks"
git push
