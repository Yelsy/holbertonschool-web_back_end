#!/usr/bin/env python3
"""function produces 10 random floating-point numbers,
and there is a 1-second pause between each number generation"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ generate random numbers waiting 1 second """
    for _ in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
