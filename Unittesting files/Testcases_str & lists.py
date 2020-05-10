"""created on Monday 18 feb 16:53:34 2020

@author: nkalyan🤠
        Implementing unit testing on Python programs for Iterators, Sequences and loops"""
import unittest
from HW04_nikhil_kalyan import count_vowels, find_last, my_enumerate
from HW04_nikhil_kalyan import my_enumerate, find_target, random_int_gen, test_gen


class CountVowelsTest (unittest.TestCase):
    def test_count_vowels(self):
        """ testing count vowels """
        string = 'Nicky'
        self.assertEqual(count_vowels(string), 1)
        self.assertEqual(count_vowels('hello world'), 3)
        self.assertEqual(count_vowels('hEllO wrld'), 2)
        self.assertEqual(count_vowels('hll wrld'), 0 )
        self.assertEqual(count_vowels('hello!hi!how are you whatareyou?'), 13)


class FindLastTest (unittest.TestCase):
    def test_find_last(self) -> None:
        """ testing find_last """
        string = 'nicky'
        self.assertEqual(find_last('o', 'Hologram'), 3)
        self.assertEqual(find_last('u', 'Barbecue'), len('Barbecue') - 2)
        self.assertEqual(find_last('e', 'Intelligence'), len('Intelligence') -1 )
        self.assertEqual(find_last('i', 'nicky'), string.count('i'))
        self.assertEqual(find_last('x', string), None)


class EnumerateTest(unittest.TestCase):
    def test_enumerate_list(self) -> None :
        """ test my_enumerate by storing the results in a list """
        self.assertEqual(list(my_enumerate('hi!howareyou?')), list(enumerate('hi!howareyou?')))
        self.assertNotEqual(list(my_enumerate('hi!howareyou?')), list(enumerate('hi!howareyou')))


class FindTargetTest(unittest.TestCase):
    def test_random_generator(self) -> None :
        """ verify RandomGenerator correct """
        random_value = next(random_int_gen(5, 5))
        self.assertTrue(random_value, 5)

    def test_find_target(self) -> None:
        """ verify find_target works for special case """
        self.assertEqual(find_target(5, 5, 5, 1), 0)
        self.assertNotEqual(find_target(4, 5, 10, 5), 1)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)