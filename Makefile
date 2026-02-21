install:
	pip install -e ".[dev]"

test:
	pytest -v

test-coverage:
	pytest --cov=gendiff --cov-report=xml --cov-report=term

lint:
	flake8 gendiff tests

lint-fix:
	autopep8 --in-place --recursive gendiff tests

check: test lint

.PHONY: install test test-coverage lint lint-fix check
