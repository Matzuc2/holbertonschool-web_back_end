#!/usr/bin/env python3
"""
Pagination module with Server class implementation.
This module provides a Server class that handles pagination for CSV data.
"""
import csv
import math
from typing import List, Dict, Any


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Retrieve a page of data with hypermedia pagination metadata.

        Args:
            page (int): Page number (1-indexed). Defaults to 1.
            page_size (int): Number of items per page. Defaults to 10.

        Returns:
            Dict[str, Any]: Dictionary containing the following keys:
                - page_size: length of the returned dataset page
                - page: current page number
                - data: dataset page (equivalent to get_page(page, page_size))
                - next_page: number of the next page, None if no next page
                - prev_page: number of the previous page, None if no prev page
                - total_pages: total number of pages in the dataset
        """
        data = self.get_page(page, page_size)
        data_length = len(self.dataset())
        total_pages = (data_length / page_size) + 1
        if page + 1 > total_pages:
            page_next = None
        else:
            page_next = page + 1
        if (page - 1) < 1:
            page_prev = None
        else:
            page_prev = page - 1
        data0 = page - 1
        return {'page_size': page_size, 'page': page, 'data': data,
                'next_page': page_next, 'prev_page': page_prev,
                'total_pages': int(total_pages)}
