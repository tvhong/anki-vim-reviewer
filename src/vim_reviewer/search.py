# -*- coding: utf-8 -*-
#
# Copyright: (c) 2025 Vy Hong <shiweistg@gmail.com>
# License: GNU AGPLv3 <https://www.gnu.org/licenses/agpl.html>

"""
Search functionality for vim reviewer.

Contains search-related classes and enums for handling vim-style search operations.
"""

import json
from dataclasses import dataclass
from enum import Enum
from aqt import Qt
from aqt.webview import AnkiWebView


class SearchMode(Enum):
    """Search mode state for vim reviewer."""

    INACTIVE = "inactive"
    FORWARD = "forward"
    BACKWARD = "backward"


@dataclass
class SearchState:
    """Model for storing search state."""

    mode: SearchMode = SearchMode.INACTIVE
    query: str = ""
    current_match: int = 0
    total_matches: int = 0
    is_input_active: bool = False


class SearchHandler:
    """Handles search-related vim key functionality."""

    def __init__(self, webview: AnkiWebView):
        self.webview: AnkiWebView = webview
        self.search_state: SearchState = SearchState()

    def is_input_active(self) -> bool:
        """Check if search input is currently active."""
        return self.search_state.is_input_active

    def handle_initiation_keys(self, key: str) -> bool:
        """Handle search initiation keys (/ and ?)."""
        if key == "/":
            self.search_state.mode = SearchMode.FORWARD
            self.search_state.is_input_active = True
            self.search_state.query = ""
            self._refresh_ui()
            return True
        elif key == "?":
            self.search_state.mode = SearchMode.BACKWARD
            self.search_state.is_input_active = True
            self.search_state.query = ""
            self._refresh_ui()
            return True
        return False

    def handle_navigation_keys(self, key: str) -> bool:
        """Handle search navigation keys (n and N)."""
        if key == "n" and self.search_state.mode != SearchMode.INACTIVE:
            self._search_next()
            return True
        elif key == "N" and self.search_state.mode != SearchMode.INACTIVE:
            self._search_previous()
            return True
        return False

    def handle_input(self, key: str, key_code: int) -> bool:
        """Handle keyboard input while in search mode."""
        if key_code == Qt.Key.Key_Return or key_code == Qt.Key.Key_Enter:
            # Execute search
            self.search_state.is_input_active = False
            self._execute_search()
            return True
        elif key_code == Qt.Key.Key_Escape:
            # Cancel search
            self.search_state.mode = SearchMode.INACTIVE
            self.search_state.is_input_active = False
            self.search_state.query = ""
            self._refresh_ui()
            return True
        elif key_code == Qt.Key.Key_Backspace:
            # Remove last character
            if self.search_state.query:
                self.search_state.query = self.search_state.query[:-1]
                self._refresh_ui()
            return True
        elif self._is_printable_char(key):
            # Add character to search query
            self.search_state.query += key
            self._refresh_ui()
            return True

        return True  # Handle all inputs while in search mode

    def _execute_search(self):
        """Execute the search with current query."""
        if not self.search_state.query:
            return

        direction = (
            "forward" if self.search_state.mode == SearchMode.FORWARD else "backward"
        )
        self.webview.eval(f"performSearch('{self.search_state.query}', '{direction}')")

    def _search_next(self):
        """Move to next search result."""
        if self.search_state.query:
            self.webview.eval("searchNext()")

    def _search_previous(self):
        """Move to previous search result."""
        if self.search_state.query:
            self.webview.eval("searchPrevious()")

    def _refresh_ui(self):
        """Refresh the UI based on current search state."""
        state_dict = {
            "mode": self.search_state.mode.value,
            "query": self.search_state.query,
            "currentMatch": self.search_state.current_match,
            "totalMatches": self.search_state.total_matches,
            "isInputActive": self.search_state.is_input_active,
        }

        state_json = json.dumps(state_dict)
        self.webview.eval(f"refresh({state_json})")

    def _is_printable_char(self, key: str):
        return len(key) == 1 and key.isprintable()
