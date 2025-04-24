#!/usr/bin/env python3
"""aaaa function"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns `n` instances of the `task_wait_random`
    coroutine with the specified `max_delay` and returns a list of all
    the delays.

    Args:
        n (int): The number of `task_wait_random` coroutines to spawn.
        max_delay (int): The maximum delay for each coroutine.

    Returns:
        List[float]: A list of delay values returned by the coroutines.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
