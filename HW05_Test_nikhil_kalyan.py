"""
Created on Saturday 22 feb 04:53:34 2020

@author: nkalyan🤠
        '''Implementing test cases on Python Scripts on strings and file '''
"""


import unittest
from HW05_nikhil_kalyan import reverse_string, find_second, get_lines, sub_string


class ReverseTest(unittest.TestCase):
    """ test reverse function """
    def test_reverse_string(self):
        """ verify that reverse string function works properly """
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("789"), "987")
        self.assertEqual(reverse_string("vedanta"), "atnadev")


class SubstringTest(unittest.TestCase):
    """Test substring function"""
    def test_sub_string(self):
        """Verify substring works properly"""
        string: str = "Hello"
        var_name: str = "Iam Groot"
        self.assertEqual(sub_string("He", string), string.find('He'))
        self.assertEqual(sub_string('n', var_name), var_name.find("n"))
        self.assertNotEqual(sub_string('Groot', var_name), var_name.find("I am"))


class FindSecondTest(unittest.TestCase):
    """ test find_second """
    def test_find_second(self):
        """ verify that find_second works properly """
        self.assertTrue(find_second('Tony', 'TonyTonystark') == 4)
        self.assertTrue(find_second('abba', 'abbabba') == 3)
        self.assertTrue(find_second(' ', 'avengers') == -1)
        self.assertEqual ( find_second('ba', 'babablacksheep'), 2)


class GetLinesTest(unittest.TestCase):
    """ test get_lines """
    def test_get_lines(self):
        """ verify that get_lines works properly """
        path_name = 'text.txt'
        file_name = 'C:/Users/NICKY/PycharmProjects/SWW810/SSW810 Homework/text1.txt'
        expect1 = []
        expect: List[str] = ['<line0>', '<line1>', '<line2>', '<line3.1 line3.2 line3.3>',
                             '<line4.1 line4.2>', '<line5>', '<line6>']
        result = list(get_lines(file_name))
        self.assertEqual(result, expect)
        self.assertEqual(list(get_lines(path_name)), expect1)
        self.assertEqual(list(get_lines(file_name)), result)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)