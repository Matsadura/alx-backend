#!/usr/bin/env python3
"""
This function named index_range takes two integer
arguments page and page_size
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns a tuple of the starting index and the end for pagination"""
    return (page*page_size - page_size, page*page_size)
