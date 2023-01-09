#!/usr/bin/env python3
"""
task 3 modules
"""
import asyncio


task = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    return the tasks
    """
    return asyncio.create_task(task(max_delay))
