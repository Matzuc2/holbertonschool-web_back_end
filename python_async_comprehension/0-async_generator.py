#!/usr/bin/env python3
"""
This module contains asynchronous generator that yields random numbers.
"""

import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronously generates 10 random numbers between 0 and 10, one at a time.

    Yields:
        float: A random number between 0 and 10.
    """
    for i in range(1, 11):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
