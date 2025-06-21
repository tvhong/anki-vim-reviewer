# Development commands for anki-vim-reviewer

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
    uv run pytest tests/

# Setup git hooks using pre-commit
setup-hooks:
    uv run pre-commit install
