#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


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
        This method returns a dictionary with the following key-value pairs:

        index: the current start index of the return page. That is the index of
        the first item in the current page. For example if requesting page 3
        with page_size 20, and no data was removed from the dataset,
        the current index should be 60.

        next_index: the next index to query with. That should be the index of
        the first item after the last item on the current page.

        page_size: the current page size

        data: the actual page of the dataset
        """
        focus = []
        idx_data = self.indexed_dataset()
        if index is None:
            index = 0
        elif index >= len(idx_data):
            index = len(idx_data) - 1
        all_keys = sorted(idx_data.keys())
        assert index >= 0 and index <= all_keys[-1]
        [focus.append(i)
         for i in all_keys if i >= index and len(focus) <= page_size]
        data = [idx_data[j] for j in focus[:-1]]
        next_idx = focus[-1] if len(focus) - page_size == 1 else None

        return {
            'index': index,
            'next_index': next_idx,
            'page_size': page_size,
            'data': data
            }
