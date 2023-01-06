#!/usr/bin/env python3
"""
a function that returns sum of floats
"""
import math


def sum_list(input_list: float) -> float:
    """
    return sum of list elemets
    """
    sum_list: float = 0.0
    for i in input_list:
        sum_list += i
    return float(sum_list)
