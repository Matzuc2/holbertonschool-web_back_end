#!/usr/bin/env python3
"""
This module provides a function to create a tuple.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple from a string and the square of a number.

    Args:
        k (str): The string to include in the tuple.
        v (Union[int, float]): The number to square and include in the tuple.

    Returns:
        Tuple[str, float]: A tuple where the first element is the string `k`
        and the second element is the square of `v` as a floating-point number.
    """
    return (k, float(v * v))
