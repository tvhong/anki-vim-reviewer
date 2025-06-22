# Design

## Overview

This is an Anki plugin that aims to implement some VIM keybindings in Anki reviewer code.
There are 2 types of keybindings we want to support:

1. Movement keys with j and k
2. Search keys with / and ? to start. Then n and N for searching forward or backward.

## Architecture

### Handling keypresses

Anki uses PyQt and manages the keystrokes before passing it to a webview.

Hence, this plugin first create Python hooks into Anki events to inject javascript code.
Then, it sets up an event filter (VimKeyEventFilter) to intercept all keypresses from PyQt.

The event filter will determine whether it should capture the event, depending on its internal state.

### UI setup

We'll follow MVVM pattern here, where Python will control the search model and
calling a `refresh(state)` method in Javascript to render the changes. The view will
be in javascript. The viewmodel will be controlled by controlled in Python and
passed to refresh as a state.

# TODOs

## Unit Testing

### Search Module Tests (tests/test_search.py)

- [x] Test SearchHandler.handle_initiation_keys() with / and ? keys
- [x] Test SearchHandler.handle_initiation_keys() with invalid keys
- [x] Test SearchHandler.handle_navigation_keys() with n and N keys
- [ ] Refactor the test to use a fixture for webview
- [ ] Refactor the tests to use parameterization for handle_navigation_keys tests
- [ ] Test SearchHandler.handle_input() with Enter/Return key
- [ ] Test SearchHandler.handle_input() with Escape key
- [ ] Test SearchHandler.handle_input() with Backspace key
- [ ] Test SearchHandler.handle_input() with printable characters
- [ ] Test SearchHandler state transitions during search workflow

- [ ] searchNext() in JS should just be searchForward()

### Movement Module Tests (tests/test_movement.py)

- [ ] Test MovementHandler initialization with config
- [ ] Test MovementHandler.handle_keys() with j key
- [ ] Test MovementHandler.handle_keys() with k key
- [ ] Test MovementHandler.handle_keys() with J key (Shift+J)
- [ ] Test MovementHandler.handle_keys() with K key (Shift+K)
- [ ] Test MovementHandler.handle_keys() with invalid keys
- [ ] Test scroll distance calculations from config

### Util Module Tests (tests/test_util.py)

- [ ] Test inject_js() with Reviewer context (should inject JS)
- [ ] Test inject_js() with non-Reviewer context (should not inject JS)
- [ ] Test inject_js() with None context

### Integration Tests (tests/test_integration.py)

- [ ] Test complete search workflow (initiate -> input -> execute -> navigate)
- [ ] Test search mode state management across multiple operations
- [ ] Test interaction between movement and search handlers
- [ ] Mock webview.eval() calls and verify correct JavaScript execution

### Test Coverage and Quality

- [ ] Set up test coverage reporting
- [ ] Achieve >80% test coverage for core modules
- [ ] Add performance tests for key handler methods
- [ ] Test error handling and edge cases

- [ ] Install itself so we can do from vim_reviewer `import \*`

## Fix bugs

- [ ] Fix space moving down during search?
- [ ] Fix backspace doesn't remove char
- [ ] Fix Enter doesn't remove cursor

## Continue Search Implementation

- [ ] Implement n/N for next/previous search results

## Testing and Polish

- [ ] Only print if debug is enabled
- [ ] Test all vim key combinations (j/k/J/K, /, ?, n/N)
- [ ] Fix any remaining keyboard event conflicts
- [ ] Add configuration options for search behavior
- [ ] Verify event filter installation/removal works properly
- [ ] Test across different Anki card types

### Improve VimReviewerConfig

- [ ] Configure VimReviewerConfig to throw an exception when a value is edge case (invalid type, negative, or xyz)
- [ ] Validate configuration with VimReviewerConfig
