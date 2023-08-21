#!/usr/bin/env python3
"""
Created by Jenaide Sibolie
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> [int, int]:
    """
    a function that takes two integer arguments that returns a tuple 
    of size of two containing start and end index.
    """
    if page <= 0 or page_size <= 0:
        raise ValueError("Both page and page_size must be greater than 0.")
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
