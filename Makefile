.PHONY: help install clean format format-fix lint lint-fix type spell check test run release docs-build docs-serve docs-clean pre-commit

help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  help             Show help."
	@echo ""
	@echo "  install          Install Python + Node deps and pre-commit hooks."
	@echo "  clean            Remove tool caches and coverage artifacts."
	@echo ""
	@echo "  format           Check formatting (Ruff, Prettier, rstfmt)."
	@echo "  format-fix       Apply formatting fixes."
	@echo "  lint             Lint Python (Ruff)."
	@echo "  lint-fix         Auto-fix Python lint issues (Ruff)."
	@echo "  type             Type-check Python (Mypy)."
	@echo "  spell            Spell-check files (cspell)."
	@echo "  check            Run all quality checks."
	@echo ""
	@echo "  test             Run tests (pytest)."
	@echo "  run              Run the project CLI."
	@echo "  release          Run semantic-release."
	@echo ""
	@echo "  docs-build       Build docs (Sphinx)."
	@echo "  docs-serve       Serve docs with live reload."
	@echo "  docs-clean       Remove docs build artifacts."
	@echo ""
	@echo "  pre-commit       Run all pre-commit hooks."

install:
	poetry install --with test,lint,mypy,docs
	npm install
	poetry run pre-commit install

clean:
	rm -rf .ruff_cache .mypy_cache .cspellcache .pytest_cache htmlcov coverage.xml junit.xml .coverage

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
