#!/usr/bin/env python3
"""
A program to add type annotation to function
"""
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """
    retriving the value from a dic using a given value
    """
    if key in dct:
        return dct[key]
    else:
        return default
