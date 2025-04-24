#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine that waits for a random delay
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for random delay between 0 and max_delay
    (inclusive) seconds and returns the delay value.
    """
    random_number = random.uniform(0, max_delay)
    await asyncio.sleep(random_number)
    return random_number
