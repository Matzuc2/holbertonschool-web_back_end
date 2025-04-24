#!/usr/bin/env python3
"""
This module contains a function to measure the average runtime of
executing the `wait_n` coroutine `n` times with a given `max_delay`.
"""

import asyncio
import time
from typing import Union
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for running `wait_n` and returns
    the average time per coroutine.

    Args:
        n (int): The number of coroutines to execute.
        max_delay (int): The maximum delay for each coroutine.

    Returns:
        float: The average runtime per coroutine.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total_time = end - start
    return total_time / n
