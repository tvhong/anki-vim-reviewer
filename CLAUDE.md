# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an Anki add-on that provides vim-style navigation and search functionality for the reviewer interface. The add-on consists of:

- **Python backend** (`src/vim_reviewer/`): Handles Anki integration, event filtering, and web content modification
- **JavaScript frontend** (`web/reviewer.js`): Implements search UI and browser-native search functionality
- **Configuration** (`config.json`): Defines scroll distances for different key combinations

## Architecture

The add-on uses a hybrid Python/JavaScript architecture with MVVM pattern:

### Python Components

- **VimKeyEventFilter**: Qt event filter that intercepts keyboard events before PyQt processes them
- **SearchHandler**: Manages search state and coordinates between Python and JavaScript
- **MovementHandler**: Handles vim movement keys (j/k/J/K) with configurable scroll distances
- **VimEventFilterManager**: Manages installation/removal of event filter during reviewer lifecycle

### Event Handling Architecture

1. **Event Interception**: Uses `QObject.eventFilter()` to capture `ShortcutOverride` and `KeyPress` events on the main window
2. **State Management**: Python maintains search state and passes it to JavaScript via `refresh(state)` calls
3. **UI Rendering**: JavaScript handles all UI updates based on state changes from Python

### Key Integration Points

- Event filter installed on `reviewer_did_show_question` and removed on `reviewer_will_end`
- JavaScript injected via `webview_will_set_content` hook using `mw.addonManager.setWebExports()`
- Configuration loaded from Anki's add-on config system and passed to handlers
- Search functionality uses browser's native `window.find()` API for text matching

## Development Setup

This project uses UV for Python dependency management:

```bash
# Install dependencies
uv sync

# Development dependencies include Anki and debugging tools
uv add --dev anki aqt pudb
```

### Development Commands

This project uses `just` for common development tasks:

```bash
# Sync dependencies
just sync

# Lint code with ruff
just lint

# Format code with ruff
just format

# Run both lint and format
just check

# Fix linting issues automatically
just fix

# Run tests with pytest
just test

# Setup pre-commit hooks
just setup-hooks
```

Run individual tests:

```bash
# Run specific test file
uv run python -m pytest tests/test_search.py -v

# Run specific test method
uv run python -m pytest tests/test_search.py::test_search_handler_handle_initiation_keys_forward_slash -v
```

### Pre-commit Hooks

The project uses pre-commit hooks that automatically run ruff linting and formatting on commit. Install them with:

```bash
just setup-hooks
# or directly: uv run pre-commit install
```

## File Structure

- `src/vim_reviewer/main.py`: Entry point and addon initialization
- `src/vim_reviewer/event_filter.py`: VimKeyEventFilter and VimEventFilterManager classes
- `src/vim_reviewer/search.py`: SearchHandler for search state management
- `src/vim_reviewer/movement.py`: MovementHandler for j/k/J/K scroll behavior
- `src/vim_reviewer/config.py`: Configuration management classes
- `src/vim_reviewer/logger.py`: Logging utility
- `src/vim_reviewer/util.py`: Utility functions (JS injection, character validation)
- `web/reviewer.js`: JavaScript UI for search functionality
- `config.json`: Default configuration for scroll distances
- `design.md`: Detailed architecture documentation and TODO list
- `justfile`: Development commands for linting and formatting

## Testing

Test manually by:

1. Installing the add-on in Anki development environment
2. Opening reviewer and testing keyboard shortcuts:
    - `j/k`: scroll down/up with configurable distances
    - `J/K`: page down/up with larger scroll distances
    - `/`: search forward (shows search bar)
    - `?`: search backward (shows search bar)
    - `Enter`: execute search
    - `Escape`: cancel search
    - `n/N`: next/previous search results

## Configuration

Scroll distances are configurable via Anki's add-on configuration:

- `j_scroll_distance`, `k_scroll_distance`: Fine scroll (default: 50px)
- `Shift_J_scroll_distance`, `Shift_K_scroll_distance`: Page scroll (default: 150px)

## Known Issues

Based on the current TODO list in `design.md`, the following features/bugs are known:

- Search functionality exists but some input handling issues remain (backspace, enter key)
- Next/previous search navigation (n/N) is partially implemented
- Unit tests have been added for config and search modules
- Some edge cases in event handling during search mode

## Workflow

- Find the next step in the TODO list under design.md
- Always run `just check` before committing to ensure code quality
