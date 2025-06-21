# -*- coding: utf-8 -*-
#
# Copyright: (c) 2025 Vy Hong <shiweistg@gmail.com>
# License: GNU AGPLv3 <https://www.gnu.org/licenses/agpl.html>

"""
Configuration management for vim reviewer.
"""

from typing import Any, cast
from dataclasses import dataclass


@dataclass
class VimReviewerConfig:
    """Configuration for vim reviewer with proper typing."""

    j_scroll_distance: int = 50
    k_scroll_distance: int = 50
    shift_j_scroll_distance: int = 150
    shift_k_scroll_distance: int = 150

    @classmethod
    def from_dict(cls, config_dict: dict[str, Any]) -> "VimReviewerConfig":
        """Create config from dictionary with safe type conversion."""
        return cls(
            j_scroll_distance=cast(int, config_dict.get("j_scroll_distance", 50)),
            k_scroll_distance=cast(int, config_dict.get("k_scroll_distance", 50)),
            shift_j_scroll_distance=cast(
                int, config_dict.get("Shift_J_scroll_distance", 150)
            ),
            shift_k_scroll_distance=cast(
                int, config_dict.get("Shift_K_scroll_distance", 150)
            ),
        )
