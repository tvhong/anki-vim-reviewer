# -*- coding: utf-8 -*-
#
# Copyright: (c) 2025 Vy Hong <shiweistg@gmail.com>
# License: GNU AGPLv3 <https://www.gnu.org/licenses/agpl.html>

"""
Event filter classes for handling vim-style keyboard events in Anki reviewer.
"""

from typing import cast
from aqt import mw
from aqt.qt import QObject, QEvent, QKeyEvent
from aqt.webview import AnkiWebView

from .config import VimReviewerConfig
from .search import SearchHandler
from .movement import MovementHandler
from .logger import Logger

# Create logger instance
logger = Logger("vim_reviewer", "INFO")


class VimKeyEventFilter(QObject):
    """Event filter to intercept keyboard events before PyQt processes them."""

    def __init__(
        self,
        webview: AnkiWebView,
        config: VimReviewerConfig,
    ) -> None:
        super().__init__()
        self.webview: AnkiWebView = webview
        self.config: VimReviewerConfig = config

        self.search_handler = SearchHandler(webview)
        self.movement_handler = MovementHandler(webview, config)

    # Override the eventFilter method to handle keyboard events
    def eventFilter(self, source: QObject, event: QEvent) -> bool:
        """Filter keyboard events and handle vim-style keys."""
        # Only handle events from main window (where we installed the filter)
        if source != mw:
            return False

        if event.type() == QEvent.Type.ShortcutOverride:
            # Prevent shortcuts for vim keys, but don't perform actions
            event = cast(QKeyEvent, event)
            if self._is_vim_key(event):
                logger.debug(f"Preventing shortcut for vim key: {event.text()}")
                event.accept()
                return True
        elif event.type() == QEvent.Type.KeyPress:
            # Actually perform vim actions
            event = cast(QKeyEvent, event)
            if self._handle_vim_key(event):
                logger.debug(f"Handled vim key action: {event.text()}")
                return True

        return False  # Pass through other events to Anki

    def _is_vim_key(self, event: QKeyEvent) -> bool:
        """Check if this is a vim key we want to handle, without performing actions."""
        key = event.text()

        if self.search_handler.is_input_active():
            return True  # Handles all keys while input is active

        return key in ["j", "k", "J", "K", "/", "?", "n", "N"]

    def _handle_vim_key(self, event: QKeyEvent) -> bool:
        """Handle vim-style keyboard shortcuts."""
        key = event.text()
        key_code = event.key()

        if self.search_handler.is_input_active():
            return self.search_handler.handle_input(key, key_code)

        if self.search_handler.handle_initiation_keys(key):
            return True

        if self.search_handler.handle_navigation_keys(key):
            return True

        if self.movement_handler.handle_keys(key):
            return True

        return False


class VimEventFilterManager:
    """Manages the installation and removal of vim event filter."""

    def __init__(self, config: VimReviewerConfig):
        self.config: VimReviewerConfig = config

        self._vim_event_filter: VimKeyEventFilter | None = None

    def install(self):
        """Install the vim event filter on the view."""
        if self._vim_event_filter is not None:
            # Already installed
            return

        # Install filter on main window to capture ShortcutOverride events before application shortcuts
        if mw and mw.web:
            self._vim_event_filter = VimKeyEventFilter(mw.web, self.config)
            mw.installEventFilter(self._vim_event_filter)
            logger.info("Vim event filter installed on main window")

    def remove(self):
        """Remove the vim event filter from the view."""
        if self._vim_event_filter is None:
            return

        if mw:
            mw.removeEventFilter(self._vim_event_filter)
            self._vim_event_filter = None
            logger.info("Vim event filter removed from main window")
