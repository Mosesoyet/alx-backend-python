#!/usr/bin/env python3
"""
Basic Async Syntax's module
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    awaits for random number of seconds
    """
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
