#!/usr/bin/env python3
""" regular function """
import asyncio
import time


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 0) -> asyncio.Task:
    """
    args: max_delay
    return: asyncio Task
    """
    task = asyncio.create_task(wait_random(max_delay))

    return task
