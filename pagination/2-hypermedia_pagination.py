#!/usr/bin/env python3
"""script pagination"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """return a tuple of size two containing a start index and an end index"""
    start_index = (page - 1) * page_size
    last_index = page * page_size

    return (start_index, last_index)


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
        """return the pagination """
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        pagen = index_range(page, page_size)
        if pagen[0] > len(self.dataset()) or pagen[1] > len(self.dataset()):
            return list()
        return [self.dataset()[i] for i in range(pagen[0], pagen[1])]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """return dictionary of hyper"""
        nextPage = None if page * \
            page_size >= len(self.dataset()) else page + 1
        return {
            'page_size': len(self.get_page(page, page_size)),
            'page': page,
            'data': self.get_page(page, page_size),
            'nextPage': nextPage,
            'prev_page': None if page == 1 else page - 1,
            'total_pages': math.ceil(len(self.dataset()) / page_size)
        }
