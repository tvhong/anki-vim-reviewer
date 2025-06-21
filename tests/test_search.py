# -*- coding: utf-8 -*-
#
# Copyright: (c) 2025 Vy Hong <shiweistg@gmail.com>
# License: GNU AGPLv3 <https://www.gnu.org/licenses/agpl.html>

"""
Tests for vim_reviewer.search module.
"""

from unittest.mock import Mock, MagicMock
from vim_reviewer.search import SearchHandler, SearchMode


def test_search_handler_handle_initiation_keys_forward_slash():
    """Test SearchHandler.handle_initiation_keys() with / key."""
    # Mock the webview
    mock_webview = Mock()
    mock_webview.eval = MagicMock()

    # Create SearchHandler instance
    handler = SearchHandler(mock_webview)

    # Test forward search initiation with /
    result = handler.handle_initiation_keys("/")

    # Verify the method returns True (handled the key)
    assert result is True

    # Verify search state was updated correctly
    assert handler.search_state.mode == SearchMode.FORWARD
    assert handler.search_state.is_input_active is True
    assert handler.search_state.query == ""

    # Verify UI refresh was called with correct refresh command
    mock_webview.eval.assert_called_once()
    call_args = mock_webview.eval.call_args[0][0]
    assert call_args.startswith("refresh(")


def test_search_handler_handle_initiation_keys_backward_question():
    """Test SearchHandler.handle_initiation_keys() with ? key."""
    # Mock the webview
    mock_webview = Mock()
    mock_webview.eval = MagicMock()

    # Create SearchHandler instance
    handler = SearchHandler(mock_webview)

    # Test backward search initiation with ?
    result = handler.handle_initiation_keys("?")

    # Verify the method returns True (handled the key)
    assert result is True

    # Verify search state was updated correctly
    assert handler.search_state.mode == SearchMode.BACKWARD
    assert handler.search_state.is_input_active is True
    assert handler.search_state.query == ""

    # Verify UI refresh was called with correct refresh command
    mock_webview.eval.assert_called_once()
    call_args = mock_webview.eval.call_args[0][0]
    assert call_args.startswith("refresh(")


def test_search_handler_handle_initiation_keys_invalid_key():
    """Test SearchHandler.handle_initiation_keys() with invalid keys."""
    # Mock the webview
    mock_webview = Mock()
    mock_webview.eval = MagicMock()

    # Create SearchHandler instance
    handler = SearchHandler(mock_webview)

    # Store initial state
    initial_mode = handler.search_state.mode
    initial_input_active = handler.search_state.is_input_active
    initial_query = handler.search_state.query

    # Test with various invalid keys
    invalid_keys = ["a", "1", "Enter", "Escape", "n", "N", "j", "k"]

    for key in invalid_keys:
        result = handler.handle_initiation_keys(key)

        # Verify the method returns False (did not handle the key)
        assert result is False

        # Verify search state was not changed
        assert handler.search_state.mode == initial_mode
        assert handler.search_state.is_input_active == initial_input_active
        assert handler.search_state.query == initial_query

    # Verify UI refresh was never called
    mock_webview.eval.assert_not_called()
