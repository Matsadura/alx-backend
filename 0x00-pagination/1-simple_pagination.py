#!/usr/bin/env python3
"""
This function named index_range takes two integer
arguments page and page_size
"""
from typing import Tuple, List
import csv
import math


def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
    """returns a tuple of the starting index and the end for pagination"""
    return (page*page_size - page_size, page*page_size)


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
        """This method returns a page of data from the dataset"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start_idx, end_idx = index_range(self, page, page_size)
        dataset = self.dataset()

        if start_idx >= len(dataset):
            return []
        return dataset[start_idx:end_idx]
