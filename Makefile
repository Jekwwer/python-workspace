# Makefile: Simplifies common development tasks.

.PHONY: help format format-fix lint lint-fix type spell test run release  docs-build docs-serve docs-clean

help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  help             Show this help message."
	@echo ""
	@echo "  format           Verify formatting in Python files (Ruff), Prettier-supported files and reStructuredText files."
	@echo "  format-fix       Auto-format Python files (Ruff), Prettier-supported files and reStructuredText files."
	@echo "  lint             Run Ruff to lint Python files."
	@echo "  lint-fix         Run Ruff to auto-fix Python lint issues."
	@echo "  type             Run Mypy for static type checking."
	@echo "  spell            Run cspell to spell-check all files."
	@echo ""
	@echo "  test             Run pytest for your test suite."
	@echo "  run              Run the chatbot CLI (`poetry run cli`)."
	@echo "  release          Run semantic-release (via npm)."
	@echo ""
	@echo "  docs-build       Build the documentation using Sphinx."
	@echo "  docs-serve       Serve the documentation locally with live reloading."
	@echo "  docs-clean       Clean up the documentation build directory."

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

test:
	poetry run pytest

run:
	poetry run cli

release:
	npm run release

docs-build:
	poetry run sphinx-build -b html docs/source docs/build/html

docs-serve:
	poetry run sphinx-autobuild docs/source docs/build/html --open-browser --watch docs/source

docs-clean:
	rm -rf docs/source/api docs/build\
