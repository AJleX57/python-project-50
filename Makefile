install:
	pip install -e ".[dev]"

test:
	pytest -v

test-coverage:
	pytest --cov=gendiff --cov-report=xml --cov-report=term

lint:
	ruff check .

lint-fix:
	ruff check . --fix

format:
	ruff format .

check: test lint

.PHONY: install test test-coverage lint lint-fix format check