mds_machine_learning_revizor

Projet Django + chart.js + Scikit permettant de voir l'évolution de la vente des jeux vidéos depuis plusieurs années.
Datasets : Video games Sales => https://www.kaggle.com/gregorut/videogamesales


## Get started

### Install globally (not recommanded if you have multiples projects with differents version of python)

- install django on your machine `python -m pip install Django`
- go on `video games_sales_analysis_app/`
- run `python manage.py runserver`

### Install locally with pipenv

- install pipenv on your machine `pip install pipenv` for Windows user installation could be a bit different go on following tuto link for more infos
- run `pipenv install` to get all dependencies
- go on `video games_sales_analysis_app/`
- run `pipenv shell` and `python manage.py runserver` OR `pipenv run python manage.py runserver`

the pipenv environment has been setup following [this tuto](https://www.techiediaries.com/pipenv-tutorial/)