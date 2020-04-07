"""
Created on Monday 29 feb 16:53:34 2020

@author: nkalyan🤠
        '''Testing Python Scripts using unittesting '''
"""

import unittest
from HW06_nikhil_kalyan import list_copy, list_intersect, list_difference, remove_vowels, check_pwd, reorder, DonutQueue


class ListCopyTest(unittest.TestCase):
    """Test the copy list method"""

    def test_list_copy(self):
        lst1 = [3, 4, 6, 8, 'JR', 'Nick']
        self.assertEqual(list_copy(lst1), list.copy(lst1))
        self.assertEqual(list_copy(['Hulk', 'Ironman', 'Cap America']),list.copy(['Hulk', 'Ironman', 'Cap America']))
        self.assertNotEqual(list_copy(lst1), list.copy(['nick', 5, 'rogers']))


class ListIntersectTest(unittest.TestCase):
    """Test cases for List intersection method"""

    def test_list_intersect(self):
        self.assertEqual(list_intersect([1, 2, 3], [1, 2, 4]), [1, 2])
        self.assertEqual(list_intersect([4, 5, 2, 'Wanda'], [5, 'Wanda', 7, 0]), [5, 'Wanda'])
        self.assertNotEqual(list_intersect([4, 5, 6, 3], []), [5])
        self.assertEqual(list_intersect([3, 5, 5], []), [])


class ListDifferenceTest(unittest.TestCase):
    """Test cases for list difference method"""

    def test_list_difference(self):
        self.assertEqual(list_difference([1, 2, 3], [1, 2, 4]), [3])
        self.assertEqual(list_difference([1, 2, 3], [4, 5, 6]), [1, 2, 3])
        self.assertNotEqual(list_difference([2, 6, 9], [6, 7, 8]), [2, 5, 7])


class RemoveVowelTest(unittest.TestCase):
    """Testing remove vowel method"""

    def test_remove_vowels(self):
        self.assertEqual(remove_vowels("Amy is my favorite daughter"), "my favorite daughter")
        self.assertEqual(remove_vowels("Jan is my best friend"), "Jan my best friend")
        self.assertNotEqual(remove_vowels("Hello world this is IQen"), "Hello world this is IQen")


class CheckPwdTest(unittest.TestCase):
    """Testing pwd check on certain conditions"""

    def test_check_password(self):
        self.assertTrue(check_pwd('88DDnnk'))
        self.assertTrue(check_pwd('00nnLLp'))
        self.assertFalse(check_pwd('aaaaBB22'))
        self.assertFalse(check_pwd('JRJR'))
        self.assertFalse(check_pwd(" "))
        self.assertFalse(check_pwd("1NN"))
        self.assertFalse(check_pwd('43434343'))
        self.assertFalse(check_pwd("nikhil"))


class DonutQueueTest(unittest.TestCase):
    """Test cases for Donut queue methods"""

    def test_queue(self):
        dq = DonutQueue()
        self.assertIsNone(dq.next_customer())
        dq.arrive("Sujit", False)
        dq.arrive("Fei", False)
        dq.arrive("Prof JR", True)
        self.assertEqual(dq.waiting(), "Prof JR, Sujit, Fei")
        dq.arrive("Nanda", True)
        self.assertEqual(dq.waiting(), "Prof JR, Nanda, Sujit, Fei")
        self.assertEqual(dq.next_customer(), "Prof JR")
        self.assertEqual(dq.next_customer(), "Nanda")
        self.assertEqual(dq.next_customer(), "Sujit")
        self.assertEqual(dq.waiting(), "Fei")
        self.assertEqual(dq.next_customer(), "Fei")
        self.assertIsNone(dq.next_customer())


class ReorderTest(unittest.TestCase):
    """Automation Testing for reorder method """

    def test_reorder(self):
        self.assertEqual(reorder([22, -5, 8, 13, 0]), sorted([22, -5, 8, 13, 0]))
        self.assertNotEqual(reorder([22, 4, 6, 8, 29]), sorted([3, 5, 6, 8, 13]))


if __name__ == '__main__' :
    unittest.main(exit=False, verbosity=2)
