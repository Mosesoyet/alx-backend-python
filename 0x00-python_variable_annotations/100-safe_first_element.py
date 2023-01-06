#!/usr/bin/env python3
"""
Making it right
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    retrieve 1st element if exists
    """
    if lst:
        return lst[0]
    else:
        return None
