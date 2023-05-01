#!/usr/bin/env python3
""" Async Comprehensions """
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """coroutine will collect 10 random numbers using an
    async comprehensing over async_generator
    Returns:
        List[float]: return the 10 random numbers
    """
    return [number async for number in async_generator()]
