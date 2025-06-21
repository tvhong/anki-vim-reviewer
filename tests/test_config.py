# -*- coding: utf-8 -*-
#
# Copyright: (c) 2025 Vy Hong <shiweistg@gmail.com>
# License: GNU AGPLv3 <https://www.gnu.org/licenses/agpl.html>

"""
Tests for vim_reviewer.config module.
"""

from vim_reviewer.config import VimReviewerConfig


def test_vim_reviewer_config_defaults():
    """Test VimReviewerConfig dataclass creation with default values."""
    config = VimReviewerConfig()

    assert config.j_scroll_distance == 50
    assert config.k_scroll_distance == 50
    assert config.shift_j_scroll_distance == 150
    assert config.shift_k_scroll_distance == 150


def test_vim_reviewer_config_from_dict_valid_inputs():
    """Test VimReviewerConfig.from_dict() with valid inputs."""
    config_dict = {
        "j_scroll_distance": 100,
        "k_scroll_distance": 75,
        "Shift_J_scroll_distance": 200,
        "Shift_K_scroll_distance": 250,
    }
    config = VimReviewerConfig.from_dict(config_dict)

    assert config.j_scroll_distance == 100
    assert config.k_scroll_distance == 75
    assert config.shift_j_scroll_distance == 200
    assert config.shift_k_scroll_distance == 250


def test_vim_reviewer_config_from_dict_missing_keys():
    """Test VimReviewerConfig.from_dict() with missing keys (should use defaults)."""
    config_dict = {
        "j_scroll_distance": 80,
        # Missing other keys should use defaults
    }
    config = VimReviewerConfig.from_dict(config_dict)

    assert config.j_scroll_distance == 80
    assert config.k_scroll_distance == 50  # default
    assert config.shift_j_scroll_distance == 150  # default
    assert config.shift_k_scroll_distance == 150  # default


def test_vim_reviewer_config_from_dict_invalid_types():
    """Test VimReviewerConfig.from_dict() with invalid types."""
    # Test with string values that should be integers
    config_dict = {
        "j_scroll_distance": "not_a_number",
        "k_scroll_distance": "100",  # string but valid number
        "Shift_J_scroll_distance": None,
        "Shift_K_scroll_distance": 200.5,  # float instead of int
    }
    config = VimReviewerConfig.from_dict(config_dict)

    # The current implementation uses cast() which doesn't validate types
    # These assertions document the current behavior
    assert config.j_scroll_distance == "not_a_number"
    assert config.k_scroll_distance == "100"
    assert config.shift_j_scroll_distance is None
    assert config.shift_k_scroll_distance == 200.5


def test_vim_reviewer_config_edge_cases_scroll_distance():
    """Test edge cases for scroll distance values."""
    # Test with zero values
    config_dict = {
        "j_scroll_distance": 0,
        "k_scroll_distance": 0,
        "Shift_J_scroll_distance": 0,
        "Shift_K_scroll_distance": 0,
    }
    config = VimReviewerConfig.from_dict(config_dict)
    assert config.j_scroll_distance == 0
    assert config.k_scroll_distance == 0
    assert config.shift_j_scroll_distance == 0
    assert config.shift_k_scroll_distance == 0

    # Test with negative values
    config_dict = {
        "j_scroll_distance": -50,
        "k_scroll_distance": -100,
        "Shift_J_scroll_distance": -200,
        "Shift_K_scroll_distance": -150,
    }
    config = VimReviewerConfig.from_dict(config_dict)
    assert config.j_scroll_distance == -50
    assert config.k_scroll_distance == -100
    assert config.shift_j_scroll_distance == -200
    assert config.shift_k_scroll_distance == -150

    # Test with very large values
    config_dict = {
        "j_scroll_distance": 9999999,
        "k_scroll_distance": 1000000,
        "Shift_J_scroll_distance": 5000000,
        "Shift_K_scroll_distance": 2000000,
    }
    config = VimReviewerConfig.from_dict(config_dict)
    assert config.j_scroll_distance == 9999999
    assert config.k_scroll_distance == 1000000
    assert config.shift_j_scroll_distance == 5000000
    assert config.shift_k_scroll_distance == 2000000
