# pip install pytest nbmake

# run nbmake
pytest --nbmake 0*.ipynb

git add 0*.ipynb
git commit -m "Updating notebooks"
git push
