#!/usr/bin/env python3
"""Module to create  asynck function."""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ return the created asyncio Task"""
    return asyncio.create_task(wait_random(max_delay))
