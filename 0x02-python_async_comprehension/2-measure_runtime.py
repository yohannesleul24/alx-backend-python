#!/usr/bin/env python3
"""runtime for four parallel comprehensions"""

import asyncio
from time import perf_counter
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    execute async_comprehension 4 times in parallel
    using asyncio.gather
    """
    mt = perf_counter()
    task = [asyncio.create_task(async_comprehension()) for i in range(4)]
    await asyncio.gather(*task)
    elapsed = perf_counter() - mt
    return elapsed
