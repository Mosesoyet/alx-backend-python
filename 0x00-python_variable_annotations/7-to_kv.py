#!/usr/bin/env python3
"""
A program to return a tuple
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    return Tuple of string and square of int or float passed as float
    """
    return (k, float(v**2))
