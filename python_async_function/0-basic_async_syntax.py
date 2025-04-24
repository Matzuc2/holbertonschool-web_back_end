#!/usr/bin/env python3
import random

async def wait_random(max_delay: float=10) -> float:
    random_number = random.uniform(0, max_delay)
    return random_number
