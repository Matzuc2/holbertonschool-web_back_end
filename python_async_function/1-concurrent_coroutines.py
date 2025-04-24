#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine that spawns multiple
wait_random coroutines and returns a list of their results.
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns `n` instances of the `wait_random`
    coroutine with the specified `max_delay` and returns a list of all
    the delays.

    Args:
        n (int): The number of `wait_random` coroutines to spawn.
        max_delay (int): The maximum delay for each `wait_random` coroutine.

    Returns:
        List[float]: A list of delay values returned by the `wait_random` coroutines.
    """
    delays: List[float] = []
    for i in range(n):
        new_one = await asyncio.gather(wait_random(max_delay))
        delays += new_one
    return delays


