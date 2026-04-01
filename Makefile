PYTHON ?= python3

setup: install
	pre-commit install --hook-type pre-push

install:
	$(PYTHON) -m pip install -r requirements.txt

test:
	$(PYTHON) -m pytest -q

lint:
	ruff check index.py

lint-fix:
	ruff check index.py --fix

check: lint test

test-steps:
	$(PYTHON) -m pytest -q -k step1
	$(PYTHON) -m pytest -q -k step2
	$(PYTHON) -m pytest -q -k step3
	$(PYTHON) -m pytest -q -k step4
	$(PYTHON) -m pytest -q -k step5

test-step:
	$(PYTHON) -m pytest -q -k step$(STEP)