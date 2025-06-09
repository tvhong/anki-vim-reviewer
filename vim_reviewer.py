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

Copyright:  (c) 2021 Yaroslav Fedorichenko <yar.fed99@gmail.com>
License: GNU AGPLv3 or later <https://www.gnu.org/licenses/agpl.html>
"""

from anki.hooks import wrap
from aqt import mw, gui_hooks, QShortcut, QKeySequence
from aqt.main import AnkiQt
from aqt.qt import QInputDialog


if mw is None:
    raise ValueError("Mainwindow is not yet initialized")

config = mw.addonManager.getConfig(__name__)

# Search state
current_search_term = ""
search_direction = "forward"
prevActionStudyDeck: bool = True

def _scrollDown(vertical = 50):
    _scroll(abs(vertical))

def _scrollUp(vertical = 50):
    _scroll(-abs(vertical))

def _scroll(vertical):
    mw.web.eval(f"window.scrollBy(0,{vertical})")

def _search_forward():
    global current_search_term, search_direction
    search_term, ok = QInputDialog.getText(mw, "Search Forward", "Search:")
    if ok and search_term:
        current_search_term = search_term
        search_direction = "forward"
        _perform_search(search_term, True)

def _search_backward():
    global current_search_term, search_direction
    search_term, ok = QInputDialog.getText(mw, "Search Backward", "Search:")
    if ok and search_term:
        current_search_term = search_term
        search_direction = "backward"
        _perform_search(search_term, False)

def _search_next():
    global current_search_term, search_direction
    if current_search_term:
        forward = search_direction == "forward"
        _perform_search(current_search_term, forward)

def _search_previous():
    global current_search_term, search_direction
    if current_search_term:
        forward = search_direction != "forward"
        _perform_search(current_search_term, forward)

def _perform_search(search_term, forward=True):
    # Clear any existing highlights first
    # self.web.eval("window.getSelection().removeAllRanges();")

    # Use browser's find API
    direction = "false" if forward else "true"
    case_sensitive = "false"
    wrap_around = "true"
    cmd = f"window.find('{search_term}', {case_sensitive}, {direction}, {wrap_around});"
    mw.web.eval(cmd)

def add_vim_shortcuts(self: AnkiQt, _old_shortcuts: any):
    """Add VIM shortcuts to Anki."""
    if not self.state == "review":
        return

    shortcuts = [
        ("j", True, lambda: _scrollDown(config['j_scroll_distance'])),
        ("k", True, lambda: _scrollUp(config['k_scroll_distance'])),
        ("Shift+j", True, lambda: _scrollDown(config['Shift_J_scroll_distance'])),
        ("Shift+k", True, lambda: _scrollUp(config['Shift_K_scroll_distance'])),

        ("/", False, lambda: _search_forward()),
        ("?", False, lambda: _search_backward()),
        ("n", False, lambda: _search_next()),
        ("Shift+n", False, lambda: _search_previous())
    ]

    qshortcuts = []
    for key, repeat, fn in shortcuts:
        scut = QShortcut(QKeySequence(key), self, activated=fn)  # type: ignore
        scut.setAutoRepeat(repeat)
        qshortcuts.append(scut)

    self.stateShortcuts.extend(qshortcuts)

    disable_conflict_shortcuts()


def disable_conflict_shortcuts() -> None:
    global prevActionStudyDeck

    # To avoid overlapping '/' shortcut
    prevActionStudyDeck = mw.form.actionStudyDeck.isEnabled()
    mw.form.actionStudyDeck.setEnabled(False)
    print(f"Disabling conflicting shortcut actionStudyDeck")


def restore_conflict_shortcuts() -> None:
    global prevActionStudyDeck

    mw.form.actionStudyDeck.setEnabled(prevActionStudyDeck)
    print(f"Restoring conflicting shortcut actionStudyDeck: {prevActionStudyDeck}")

# Not using gui_hooks as we need to set setAutoRepeat=true for some shortcuts
AnkiQt.setStateShortcuts = wrap(
    AnkiQt.setStateShortcuts,
    add_vim_shortcuts,
    "after"
)

gui_hooks.reviewer_will_end.append(restore_conflict_shortcuts)
