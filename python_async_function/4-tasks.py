#!/usr/bin/env python3
""" Tasks """
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """async routine
    Args:
        n (int): Number of times
        max_delay (int): Waiting top number
    Returns:
        List[float]: list of all the delays
    """
    delay_list = [task_wait_random(max_delay) for _ in range(n)]
    return [await delay_list
            for delay_list in asyncio.as_completed(delay_list)]
