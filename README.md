create env

python -m jupyter notebook

python -m pip install --user virtualenv

python -m venv env

.\env\Scripts\activate

install the req

pip install -r requirements.txt
download the data from

https://drive.google.com/drive/folders/18zqQiCJVgF7uzXgfbIJ-04zgz1ItNfF5?usp=sharing

git init
dvc init 
dvc add data_given/winequality.csv
git add .
git commit -m "first commit"
oneliner updates for readme

git add . && git commit -m "update Readme.md"
git remote add origin https://github.com/c17hawke/simple-dvc-demo.git
git branch -M main
git push origin main
tox command -

tox
for rebuilding -

tox -r 
pytest command

pytest -v
setup commands -

pip install -e . 
build your own package commands-

python setup.py sdist bdist_wheel