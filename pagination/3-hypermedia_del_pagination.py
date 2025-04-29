#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Returns paginated data that's resilient to deletions.

        This method will return page_size items starting from the index,
        even if some items are deleted between requests.
        It adjusts the next_index
        value to account for any missing indices.

        Args:
            index (int): Starting index for the current page.
            page_size (int): Number of items to return per page.

        Returns:
            Dict: Dictionary containing:
                - index: Current start index
                - data: List of actual page items
                - page_size: Size of the returned page
                - next_index: Next index to query for subsequent page
        """
        data = []
        data_set = self.indexed_dataset()
        length = len(data_set)
        assert 0 <= index < length

        next_index = index + page_size
        i = index
        j = next_index

        while i < j:
            try:
                data += [data_set[i]]
            except KeyError:
                j += 1
            i += 1

        return {
            'index': index,
            'data': data,
            'page_size': page_size,
            'next_index': next_index
        }
