#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine that waits for a random delay
and returns the delay value.
"""

import random
import asyncio


async def wait_random(max_delay: float = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay
    (inclusive) seconds and returns the delay value.

    Args:
        max_delay (float): The maximum delay in seconds. Defaults to 10.

    Returns:
        float: The actual delay value.
    """
    random_number = random.uniform(0, max_delay)
    await asyncio.sleep(random_number)
    return random_number

