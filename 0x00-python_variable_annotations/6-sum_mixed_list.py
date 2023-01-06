#!/usr/bin/python3
"""
A program to sum mix list elements as float
"""
from typing import List


def sum_mixed_list(mxd_lst: List[int, float]) -> float:
    """
    return float sum of any list element
    """
    return float(sum(mxd_lst))
