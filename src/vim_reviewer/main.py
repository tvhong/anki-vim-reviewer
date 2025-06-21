# -*- coding: utf-8 -*-

"""
Anki Add-on: Vim-style Navigation and Search for Reviewer

While review window is focused:
- j/k: scroll down/up
- J/K: page down/up
- /: search forward
- ?: search backward
- n: next search result
- N: previous search result

Copyright:  (c) 2025 Vy Hong <shiweistg@gmail.com>
License: GNU AGPLv3 or later <https://www.gnu.org/licenses/agpl.html>
"""

from aqt import gui_hooks, mw

from .util import inject_js
from .config import VimReviewerConfig
from .event_filter import VimEventFilterManager


def main():
    """Initialize the vim reviewer addon."""
    if mw is None:
        raise ValueError("Mainwindow is not yet initialized")

    # Load and parse configuration
    config_dict = mw.addonManager.getConfig(__name__) or {}
    config = VimReviewerConfig.from_dict(config_dict)

    # Export javascript and css files for webview
    mw.addonManager.setWebExports(__name__, r"web/.*(css|js)")

    vim_filter_manager = VimEventFilterManager(config)

    gui_hooks.webview_will_set_content.append(inject_js)

    gui_hooks.reviewer_did_show_question.append(
        lambda _card: vim_filter_manager.install()
    )
    gui_hooks.reviewer_will_end.append(lambda: vim_filter_manager.remove())
