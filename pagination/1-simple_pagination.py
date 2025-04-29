#!/usr/bin/env python3
"""
Pagination module with Server class implementation.
This module provides a Server class that handles pagination for CSV data.
"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple containing the start and end indexes for pagination.

    Args:
        page (int): Current page number (1-indexed).
        page_size (int): Number of items per page.

    Returns:
        tuple: A tuple containing the start index and end index for
              the requested page and page size.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


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
        Retrieve a specific page of data from the dataset.

        Args:
            page (int): Page number (1-indexed). Defaults to 1.
            page_size (int): Number of items per page. Defaults to 10.

        Returns:
            List[List]: List of rows corresponding to the requested page.
        """
        results = []
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        new_list = self.dataset()
        ind = index_range(page, page_size)
        for i in range(ind[0], ind[1]):
            try:
                results += [new_list[i]]
            except IndexError:
                results = []
        return results
