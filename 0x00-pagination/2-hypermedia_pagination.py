#!/usr/bin/env python3
"""
Created by Jenaide Sibolie
"""
import csv
import math
from typing import Dict, List, Tuple



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

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initializes a new Server instance.
        """
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
        retrieves a page of data
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        retrieves the info page
        """
        page_data = self.get_page(page, page_size)
        start_index, end_index = index_range(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        info = {
            "page_size": len(page_data),
            "page": page,
            "data": page_data,
            "next_page": page + 1 if end_index < len(self.__dataset) else None,
            "prev_page": page - 1 if start_index > 0 else None,
            "total_pages": total_pages
        }
        return info
