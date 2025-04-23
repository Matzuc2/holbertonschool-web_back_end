#!/usr/bin/env python3
"""
This module provides a function to compute the sum of a list
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """
    Compute the sum of a list containing integers and floating-point numbers.

    Args:
        mxd_lst (List[Union[float, int]]): A list of integers a.

    Returns:
        float: The sum of the numbers in the list as a floating-point number.
    """
    return sum(mxd_lst)
