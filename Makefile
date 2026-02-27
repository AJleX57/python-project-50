install:
	pip install -e ".[dev]"

test:
	pytest -v

test-coverage:
	pytest --cov=gendiff --cov-report=xml --cov-report=term

test-nested:
	pytest tests/test_gendiff_nested.py -v

lint:
	flake8 gendiff tests

lint-fix:
	autopep8 --in-place --recursive gendiff tests

check: test lint

.PHONY: install test test-coverage test-nested lint lint-fix check