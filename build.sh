
cp soln/0*.ipynb .

python remove_soln.py

git add 0*.ipynb
git commit -m "Updating the notebooks"
git push
