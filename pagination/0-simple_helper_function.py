#!/usr/bin/env python3
"""
Pagination helper function module.
This module provides utility functions to handle pagination calculations.
"""


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
