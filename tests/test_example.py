#!/usr/bin/env python3

"""
Example test module
"""

import unittest

from boilerplate.example import example

class TestExample(unittest.TestCase):
    """Test example"""
    def test_example_return(self) -> None:
        """Test example exception check"""
        with self.assertRaises(NotImplementedError):
            example()
