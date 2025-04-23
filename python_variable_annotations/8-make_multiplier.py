#!/usr/bin/env python3
"""
This module provides a function to create a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a given number by a specified multiplier.

    Args:
        multiplier (float): The multiplier to use in the returned function.

    Returns:
        Callable[[float], float]: A function that takes a float as input and
        returns the product of the input and the multiplier.
    """
    def fuc(value: float) -> float:
        """
        Multiply the input value by the multiplier.

        Args:
            value (float): The number to be multiplied.

        Returns:
            float: The product of the value and the multiplier.
        """
        return value * multiplier

    return fuc
