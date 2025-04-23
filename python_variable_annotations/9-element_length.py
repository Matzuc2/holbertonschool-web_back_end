#!/usr/bin/env python3
"""
This module provides a function to compute the length of elements in an iterable of sequences.
"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Compute the length of each element in an iterable of sequences.

    Args:
        lst (Iterable[Sequence]): An iterable containing sequence elements (e.g., lists, strings, tuples).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains a sequence from the input
        and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
