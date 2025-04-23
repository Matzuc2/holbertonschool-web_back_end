#!/usr/bin/env python3
"""
This module provides a function to compute the length
"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Compute the length of each element in an iterable of sequences.

    Args:
        lst (Iterable[Sequence]): An iterable containing sequence elements

    Returns:
        List[Tuple[Sequence, int]]
        and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
