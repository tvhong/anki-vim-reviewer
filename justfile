# Development commands for anki-vim-reviewer
# Sync virtual environment
sync:
    uv sync --group dev

# Run ruff linter
lint:
    uv run ruff check src/

# Run ruff formatter
format:
    uv run ruff format src/

# Run both lint and format
check: lint format

# Fix linting issues automatically
fix:
    uv run ruff check --fix src/

# Run tests with pytest
test:
    uv run python -m pytest tests/ -v

# Setup git hooks using pre-commit
setup-hooks:
    uv run pre-commit install
