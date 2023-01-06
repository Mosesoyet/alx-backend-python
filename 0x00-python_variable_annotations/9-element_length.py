#!/usr/bin/env python3
"""
A program to annotate function as expected
"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Computes the list's length
    """
    return [(i, len(i)) for i in lst]
