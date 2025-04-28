#!/usr/bin/env python3
"""
This module contains a function to measure the runtime of executing
async_comprehension four times in parallel.
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """
    Measures the total runtime of running async four times in parallel.

    Returns:
        float: The total runtime in seconds.
    """
    tasks = [async_comprehension() for i in range(4)]
    start = time.time()
    await asyncio.gather(*tasks)
    end = time.time()
    total_time = end - start
    return total_time
