#!/usr/bin/python3
"""
Taks 1 modules
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes wait random n times
    """
    wait_times = wait asyncio.gather(
            *tuple(map(lambda _: wait_random(max_delay), range(n)))
            )
    return sorted(wait_times)
