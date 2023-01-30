#!/usr/bin/env python3
"""
Utils's test module
"""
import unittest
from typing import Dict, Tuple, Union
from unittest.mock import patch, Mock
from parameterized import parameterized

from utils import (
        access_nested_map,
        get_json,
        memoize,
)


class TestAccessNestedMap(unittest.TestCase):
    """Test access_nested_map function
    """
    @parameterized.expand([
    ({'a': 1}, ('a',), 1),
    ({'a': {'b': 2}}, ('a',), {'b': 2}),
    ({'a': {'b': 2}}, ('a', 'b'), 2),
    ])
    

    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int],
            ) -> None:
        """Test access_nested map's output
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)


    @parameterized.expand([
        ({}, ('a',), KeyError),
        ({'a': 1}, ('a', 'b'), KeyError),
        ])


    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            exception: Exception,
            ) -> None:
        """Raise exception for the above input
        """
        with self.assertRaises(exception):
            accss_nested_map(nested_map, path)
