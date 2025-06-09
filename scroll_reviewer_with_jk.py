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
from aqt import mw
from aqt.main import AnkiQt
from aqt.qt import QShortcut, QKeySequence, QInputDialog


config = mw.addonManager.getConfig(__name__) if hasattr(mw, 'addonManager') else {}

# Search state
current_search_term = ""
search_direction = "forward"

def _scrollDown(self, vertical = 50):
    _scroll(self, abs(vertical))

def _scrollUp(self, vertical = 50):
    _scroll(self, -abs(vertical))

def _scroll(self, vertical):
    self.web.eval(f"window.scrollBy(0,{vertical})")

def _search_forward(self):
    global current_search_term, search_direction
    search_term, ok = QInputDialog.getText(self, "Search Forward", "Search:")
    if ok and search_term:
        current_search_term = search_term
        search_direction = "forward"
        _perform_search(self, search_term, True)

def _search_backward(self):
    global current_search_term, search_direction
    search_term, ok = QInputDialog.getText(self, "Search Backward", "Search:")
    if ok and search_term:
        current_search_term = search_term
        search_direction = "backward"
        _perform_search(self, search_term, False)

def _search_next(self):
    global current_search_term, search_direction
    if current_search_term:
        forward = search_direction == "forward"
        _perform_search(self, current_search_term, forward)

def _search_previous(self):
    global current_search_term, search_direction
    if current_search_term:
        forward = search_direction != "forward"
        _perform_search(self, current_search_term, forward)

def _perform_search(self, search_term, forward=True):
    # Clear any existing highlights first
    self.web.eval("window.getSelection().removeAllRanges();")

    # Use browser's find API
    direction = "true" if forward else "false"
    self.web.eval(f"window.find('{search_term}', false, {direction});")

def add_vim_shortcuts(self, shortcuts):
    if not self.state == "review":
        return
    shortcuts = [
        ("j", lambda: _scrollDown(self, config.get('j_scroll_distance', 50))),
        ("k", lambda: _scrollUp(self, config.get('k_scroll_distance', 50))),
        ("Shift+J", lambda: _scrollDown(self, config.get('Shift_J_scroll_distance', 150))),
        ("Shift+K", lambda: _scrollUp(self, config.get('Shift_K_scroll_distance', 150))),
        ("/", lambda: _search_forward(self)),
        ("?", lambda: _search_backward(self)),
        ("n", lambda: _search_next(self)),
        ("N", lambda: _search_previous(self))
    ]
    qshortcuts = []
    for key, fn in shortcuts:
        scut = QShortcut(QKeySequence(key), self, activated=fn)  # type: ignore
        scut.setAutoRepeat(True)
        qshortcuts.append(scut)
    self.stateShortcuts.extend(qshortcuts)


AnkiQt.setStateShortcuts = wrap(AnkiQt.setStateShortcuts, add_vim_shortcuts)
