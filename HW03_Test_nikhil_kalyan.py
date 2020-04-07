"""
Created on Tuesday Feb 18   16:46:59 2020

@author: nkalyan🤠

    Implementing Unit testing algorithm to test the Fractions programs
"""

import unittest
from HW03_nikhil_kalyan import Fraction


class TestFraction(unittest.TestCase):
    """ test class Fraction """

    def test_init(self):
        """ verify that the numerator and denominator are set properly """
        f: Fraction = Fraction(3, 4)
        self.assertEqual(f.numerator, 3)
        self.assertEqual(f.denominator, 4)

    def test_init_exception(self) :
        """ verify that ZeroDivisionError is raised when appropriate """
        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 0)

    def test_add(self) :
        """ verify Fraction addition """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        self.assertEqual(f12 + f34, Fraction(10, 8))
        self.assertEqual(f12, Fraction(1, 2))  # f12 should not have changed

    def test_sub(self):
        """Verify Fraction Substraction"""
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        self.assertEqual(f12 - f34, Fraction(-1, 4))
        self.assertEqual(f12, Fraction(1, 2))

    def test_mul(self):
        """Verify Fraction Multiplication"""
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        self.assertEqual(f12 * f34, Fraction(3, 8))
        self.assertEqual(f12, Fraction(1, 2))

    def test_truediv(self):
        """Verify Fraction Division"""
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        self.assertEqual(f12 / f34, Fraction(2, 3))
        self.assertEqual(f12, Fraction(1, 2))

    def test_str(self):
        """Verify string"""
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        self.assertEqual(str(f12), '1 / 2')
        self.assertTrue(f12)
        self.assertTrue(f34)

    def test_ne(self):
        """Verify not equal"""
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        f23: Fraction = Fraction(-2, 3)
        self.assertNotEqual(f12, f34)
        self.assertNotEqual(f34, f12)
        self.assertNotEqual(f23, f12)
        self.assertFalse(f12 != f12)

    def test_eq(self):
        """Test for equality"""
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        f23: Fraction = Fraction(-2, 3)
        self.assertTrue(f12 == f12)
        self.assertFalse(f12 == f34)
        self.assertTrue(f34 == f34)
        self.assertEqual(f12, f12)
        self.assertFalse(f23 == f12)

    def test_le(self):
        """Verifying fraction Less than or equal"""
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        f23: Fraction = Fraction(-2, 3)
        self.assertTrue(f12 <= f12)
        self.assertTrue(f12 <= f34)
        self.assertTrue(f34 <= f34)
        self.assertLessEqual(f12, f12)
        self.assertLessEqual(f23, f12)

    def test_lt(self):
        """Verifying Fraction Less than Test"""
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        f23: Fraction = Fraction(-2, 3)
        self.assertTrue(f12 < f34)
        self.assertFalse(f34 < f12)
        self.assertLess(f12, f34)
        self.assertLess(f23, f12)

    def test_ge(self):
        """Verifying Fraction Greater than or equal Test"""
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        f23: Fraction = Fraction(-2, 3)
        self.assertTrue(f34 >= f12)
        self.assertFalse(f12 >= f34)
        self.assertTrue(f34 >= f34)
        self.assertGreaterEqual(f34, f12)
        self.assertGreaterEqual(f12, f23)

    def test_gt(self):
        """Verifying Fractions than test"""
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        f23: Fraction = Fraction(-2, 3)
        self.assertTrue(f34 > f12)
        self.assertFalse(f12 > f34)
        self.assertGreater(f34, f12)
        self.assertGreater(f12, f23)

    def test_3_operands(self):
        """ verify expressions with more than two operands """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        f44: Fraction = Fraction(4, 4)
        self.assertTrue(f12 + f34 + f44 == Fraction(72, 32))
        self.assertTrue(f12 - f34 - f44 == Fraction(-40, 32))
        self.assertTrue((f12 * f34 * f44 == Fraction(12, 32)))
        self.assertTrue((f12 / f34 / f44 == Fraction(16, 24)))

    def test_simplify(self):
        """Simplify your fraction"""
        f24 = Fraction(2, 4)
        f24s = f24.simplify()
        f927 = Fraction(-9, 27)
        f927s = f927.simplify()
        self.assertEqual(str(f24s), '1 / 2')
        self.assertEqual(str(f927s), '-1 / 3')

if __name__ == '__main__':
    """verbosity = 0(quite) : Just get total nof tests executed and global result
        verbosity = 1(default) : You get same as ) but dot for every successful test or F for failure
        verbosity = 2(Verbose) : You get help string of every test and the result
    """
    unittest.main(exit=False, verbosity=2)