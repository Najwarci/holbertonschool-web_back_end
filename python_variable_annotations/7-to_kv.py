#!/usr/bin/env python3
"""Create a tuple with a string and the square of a number."""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple of the string and the square of the number."""
    return (k, float(v ** 2))
