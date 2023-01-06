#!/usr/bin/env python3
"""
a program to return a function that multiplies an argument
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    a function that returns a function that multiplies float by multiplier
    """
    return lambda i: i * multiplier
