# Makefile: Simplifies common development tasks.

.PHONY: help install clean format format-fix lint lint-fix type spell check test run release docs-build docs-serve docs-clean pre-commit

help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  help             Show this help message."
	@echo ""
	@echo "  install          Install Python and Node dependencies."
	@echo "  clean            Remove tool caches and coverage artifacts."
	@echo ""
	@echo "  format           Verify formatting in Python files (Ruff), Prettier-supported files and reStructuredText files."
	@echo "  format-fix       Auto-format Python files (Ruff), Prettier-supported files and reStructuredText files."
	@echo "  lint             Run Ruff to lint Python files."
	@echo "  lint-fix         Run Ruff to auto-fix Python lint issues."
	@echo "  type             Run Mypy for static type checking."
	@echo "  spell            Run cspell to spell-check all files."
	@echo "  check            Run all quality checks (format, lint, type, spell)."
	@echo ""
	@echo "  test             Run pytest for your test suite."
	@echo "  run              Run the project CLI."
	@echo "  release          Run semantic-release (via npm)."
	@echo ""
	@echo "  docs-build       Build the documentation using Sphinx."
	@echo "  docs-serve       Serve the documentation locally with live reloading."
	@echo "  docs-clean       Clean up the documentation build directory."
	@echo ""
	@echo "  pre-commit       Run all pre-commit hooks against all files."

install:
	poetry install --with test,lint,mypy,docs
	npm install

clean:
	rm -rf .ruff_cache .mypy_cache .cspellcache .pytest_cache htmlcov coverage.xml .coverage

format:
	poetry run ruff format . --check
	poetry run rstfmt --check -w 120 docs/source
	npm run format

format-fix:
	poetry run ruff format .
	poetry run rstfmt -w 120 docs/source
	npm run format-fix

lint:
	poetry run ruff check .

lint-fix:
	poetry run ruff check --fix .

type:
	poetry run mypy --install-types --non-interactive src tests

spell:
	npm run spell

check: format lint type spell

test:
	poetry run pytest

run:
	poetry run cli

release:
	npm run release

docs-build:
	poetry run sphinx-build -W --keep-going -b html docs/source docs/build/html

docs-serve:
	poetry run sphinx-autobuild docs/source docs/build/html --open-browser --watch docs/source

docs-clean:
	rm -rf docs/source/api docs/build

pre-commit:
	poetry run pre-commit run --all-files
