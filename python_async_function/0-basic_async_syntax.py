#!/usr/bin/env python3
"""asynchronous coroutine that waits for 
   a random delay between 0 and max_delay"""
import asyncio
import random


async def wait_random(max_delay=10) -> float:
    """returns a random delay between 0 and max_delay"""
    delay_seconds = random.uniform(0, max_delay)
    await asyncio.sleep(delay_seconds)
    return delay_seconds
