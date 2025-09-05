#!/usr/bin/env python3
"""
Hypermedia pagination using a dataset of popular baby names.
"""

import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indexes for a given page.

    Args:
        page (int): current page number (1-indexed).
        page_size (int): number of items per page.

    Returns:
        tuple[int, int]: (start_index, end_index) for pagination.
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return the appropriate page of the dataset.

        Args:
            page (int): page number (must be > 0).
            page_size (int): number of items per page (must be > 0).

        Returns:
            List[List]: a list of rows corresponding to the page.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        dataset = self.dataset()

        if start >= len(dataset):
            return []

        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Return a dictionary containing hypermedia pagination info.

        Args:
            page (int): current page number (must be > 0).
            page_size (int): number of items per page (must be > 0).

        Returns:
            Dict: hypermedia pagination info
        """
        data = self.get_page(page, page_size)
        dataset_len = len(self.dataset())
        total_pages = math.ceil(dataset_len / page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
