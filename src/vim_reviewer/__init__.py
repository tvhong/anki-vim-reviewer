# -*- coding: utf-8 -*-
#
# Copyright: (c) 2025 Vy Hong <shiweistg@gmail.com>
# License: GNU AGPLv3 <https://www.gnu.org/licenses/agpl.html>

from .main import main

# Only initialize when running in Anki, not during tests
try:
    from aqt import mw

    if mw is not None:
        main()
except ImportError:
    # aqt not available (e.g., during testing)
    pass
