# vicuna

集群管理工具

## Install

Create a virtualenv and activate it:

- python3 :
```
python3 -m venv venv
. venv/bin/activate
```

- python2 :
```
python2 -m virtualenv venv
. venv/bin/activate
```

Install Vicuna:
```
pip install -e .
```

## Run

```
export FLASK_APP=vicuna
export FLASK_ENV=development
flask init-db
flask run
```

Open http://127.0.0.1:5000 in a browser

## Test

```
pip install '.[test]'
pytest
```

Run with coverage report:
```
coverage run -m pytest
coverage report
coverage html  # open htmlcov/index.html in a browser
```