# -*- coding: utf-8 -*-
#
# Copyright: (c) 2025 Vy Hong <shiweistg@gmail.com>
# License: GNU AGPLv3 <https://www.gnu.org/licenses/agpl.html>

from aqt import mw
from aqt.webview import WebContent
from aqt.reviewer import Reviewer


def inject_js(web_content: WebContent, context: "object | None") -> None:
    """Inject JavaScript into the web content if the context is a Reviewer."""

    if not isinstance(context, Reviewer):
        # not reviewer, do not modify content
        return

    addon_package = mw.addonManager.addonFromModule(__name__)

    web_content.js.append(f"/_addons/{addon_package}/web/reviewer.js")
