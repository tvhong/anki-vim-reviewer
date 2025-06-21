# -*- coding: utf-8 -*-
#
# Copyright: (c) 2025 Vy Hong <shiweistg@gmail.com>
# License: GNU AGPLv3 <https://www.gnu.org/licenses/agpl.html>

"""
Movement handler for vim-style navigation in Anki reviewer.

Handles j/k/J/K keys for scrolling functionality.
"""

from aqt.webview import AnkiWebView

from .config import VimReviewerConfig


class MovementHandler:
    """Handles movement-related vim key functionality."""

    def __init__(self, webview: AnkiWebView, config: VimReviewerConfig):
        self.webview: AnkiWebView = webview
        self.config: VimReviewerConfig = config

    def handle_keys(self, key: str) -> bool:
        """Handle movement keys (j/k/J/K)."""
        if key == "j":
            self.webview.eval(f"window.scrollBy(0, {self.config.j_scroll_distance})")
            return True
        elif key == "k":
            self.webview.eval(f"window.scrollBy(0, -{self.config.k_scroll_distance})")
            return True
        elif key == "J":
            self.webview.eval(
                f"window.scrollBy(0, {self.config.shift_j_scroll_distance})"
            )
            return True
        elif key == "K":
            self.webview.eval(
                f"window.scrollBy(0, -{self.config.shift_k_scroll_distance})"
            )
            return True

        return False
