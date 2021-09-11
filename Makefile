test:
	pytest -x jinja_markdown tests

lint:
	flake8 --config=setup.cfg jinja_markdown tests

coverage:
	pytest --cov-report html --cov jinja_markdown --cov tests jinja_markdown tests

setup:
	pip install -U pip wheel
	pip install -e .[dev,test]
	pre-commit install --hook-type pre-push
