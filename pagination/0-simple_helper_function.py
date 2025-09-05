#!/usr/bin/env python3
"""
Simple helper function for pagination.
"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Returns a tuple containing the start and end indexes
    for pagination parameters.

    Args:
        page (int): current page number (1-indexed).
        page_size (int): number of items per page.

    Returns:
        tuple[int, int]: (start_index, end_index).
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
