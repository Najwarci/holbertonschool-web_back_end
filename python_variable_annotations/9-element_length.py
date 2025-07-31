#!/usr/bin/env python3
"""Compute the length of elements in an iterable of sequences."""

from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples with each element and its length."""
    return [(i, len(i)) for i in lst]
