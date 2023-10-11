#!/usr/bin/env python3
"""scripts that calculates start_index and end_index"""


def index_range(page, page_size):
    """eturn a tuple of size two containing a start index and an end index"""
    start_index = (page - 1) * page_size
    last_index = page * page_size

    return (start_index, last_index)
