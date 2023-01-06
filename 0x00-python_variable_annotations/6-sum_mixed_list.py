#!/usr/bin/env python3
"""
A program to sum mix list elements as float
"""
from typing import List Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    return float sum of any list element
    """
    return sum(mxd_lst)
