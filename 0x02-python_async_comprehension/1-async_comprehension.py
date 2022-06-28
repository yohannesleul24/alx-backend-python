#!/usr/bin/env python3
"""Async comprehension that takes no arguments"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    this coroutine will collect 10 random numbers
    using async comprehension over
    async_generator, then it will return 10 random numbers
    """
    return [i async for i in async_generator()]
