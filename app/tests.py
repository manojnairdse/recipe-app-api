"""
Sample Test
"""

from django.test import SimpleTestCase

from app import calc

class ClacTect(SimpleTestCase):

    def test_add_number(self):
        res = calc.add(5,9)

        self.assertEqual(res, 14)