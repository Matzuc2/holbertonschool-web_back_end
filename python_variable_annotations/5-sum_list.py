#!/usr/bin/env python3
"""
This module provides a function to compute the sum of a list of floating-point numbers.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Compute the sum of a list of floating-point numbers.

    Args:
        input_list (List[float]): A list of floating-point numbers.

    Returns:
        float: The sum of the numbers in the list.
    """
    return sum(input_list)
