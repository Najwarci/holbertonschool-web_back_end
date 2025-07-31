#!/usr/bin/env python3
"""Sum a list of integers and floats."""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Return the sum as a float."""
    return float(sum(mxd_list))
