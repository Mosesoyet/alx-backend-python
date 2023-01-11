#!/usr/bin/env python3
"""
A program to write a couroutine that will collect 10 random numbers using async
comprehensing.
return 10 random numbers
"""
from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    generates 10 random numbers
    """
    return [num async for num in async_generator()]
