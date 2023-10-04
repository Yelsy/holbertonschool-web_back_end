#!/usr/bin/env python3
"""Measure the runtime"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """It calculates the total execution time and the average time """
    start_time = time.time() # record the start time
    await wait_n(n, max_delay)
    end_time = time.time() # record the end time

    total_time = end_time - start_time # calculate the total execution time
    average_time = total_time / n
    
    return average_time
    