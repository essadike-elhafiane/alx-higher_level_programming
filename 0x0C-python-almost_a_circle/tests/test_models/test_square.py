"""
module: test_square - used to test the square module
"""

import unittest
import io
import sys
from models.square import Square


class TestSquare(unittest.TestCase):
    def setUp(self):
        self.sq_1 = Square(3)

    def test_display(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.sq_1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "###\n###\n###\n")
