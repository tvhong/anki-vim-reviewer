# -*- coding: utf-8 -*-
#
# Copyright: (c) 2025 Vy Hong <shiweistg@gmail.com>
# License: GNU AGPLv3 <https://www.gnu.org/licenses/agpl.html>

"""
Logger module for vim reviewer.

Simple logger class to avoid conflicts with Anki's logging system.
"""


class Logger:
    """Simple logger class to avoid conflicts with Anki's logging system."""

    LEVELS: dict[str, int] = {"DEBUG": 0, "INFO": 1, "WARNING": 2, "ERROR": 3}

    def __init__(self, name: str, level: str = "INFO"):
        self.name: str = name
        self.level: str = level

    def debug(self, msg: str):
        if self._should_log("DEBUG"):
            print(f"[{self.name}] DEBUG: {msg}")

    def info(self, msg: str):
        if self._should_log("INFO"):
            print(f"[{self.name}] INFO: {msg}")

    def warning(self, msg: str):
        if self._should_log("WARNING"):
            print(f"[{self.name}] WARNING: {msg}")

    def error(self, msg: str):
        if self._should_log("ERROR"):
            print(f"[{self.name}] ERROR: {msg}")

    def _should_log(self, level: str) -> bool:
        return self.LEVELS[level] >= self.LEVELS[self.level]
