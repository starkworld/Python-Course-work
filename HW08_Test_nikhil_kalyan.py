# coding=utf-8
"""
Created on Monday 05 March 16:53:34 2020

@author: nkalyan🤠
        '''Testing Python scripts of date time differences, reading files generator and analyzing file'''
"""

import unittest
from datetime import datetime
from typing import List, Tuple

from HW08_nikhil_kalyan import date_arithmetic, file_reader, FileAnalyzer


class TestDateArithmetic(unittest.TestCase):
    """ Test for date arithmetic method """

    def test_date_arithmetic(self):
        """ test cases for date arithmetic """
        self.assertEqual(date_arithmetic(), (datetime(2020, 3, 1, 0, 0), datetime(2019, 3, 2, 0, 0), 241))
        self.assertNotEqual(date_arithmetic(), (datetime(2000, 3, 1, 0, 0), datetime(2000, 3, 2, 0, 0), 341))
        self.assertNotEqual(date_arithmetic(), '')


class TestFileReader(unittest.TestCase):
    """Test for files analyzer method"""

    def test_file_reader(self):
        """ check for file reading with header and separated by | """
        answer: List[Tuple[str]] = [each_line for each_line in file_reader('Student_major', 3, "|", True)]
        answer2: List[Tuple[str]] = [each_line for each_line in file_reader('Student_major', 3, "|", False)]
        self.assertEqual(answer,
                         [("123", "Jin He", "Computer Science"),
                          ("234", "Nanda Koka", "Software Engineering"),
                          ("345", "Benji Cai", "Software Engineering")])
        self.assertEqual(answer2,
                         [('CWID', 'Name', 'Major'),
                          ("123", "Jin He", "Computer Science"),
                          ("234", "Nanda Koka", "Software Engineering"),
                          ("345", "Benji Cai", "Software Engineering")])


class TestFileAnalyzer(unittest.TestCase):
    """Test for file analyzer method"""

    def test_file_analyzer(self):
        """Test cases for file analyser"""
        file_analyzer: FileAnalyzer = FileAnalyzer("/Users/nikhilkalyan/PycharmProjects/SSW HW08")
        self.assertEqual({'HW01_nikhil_kalyan.py': {'class': 0, 'function': 4, 'line': 82, 'char': 2480},
                          'HW02_nikhil_kalyan.py': {'class': 1, 'function': 12, 'line': 156, 'char': 6537}},
                         file_analyzer.files_summary)
        self.assertNotEqual({'HW01_nikhil_kalyan.py': {'class': 1, 'function': 4, 'line': 82, 'char': 2480},
                             'HW02_nikhil_kalyan.py': {'class': 1, 'function': 12, 'line': 156, 'char': 6537}},
                            file_analyzer.files_summary)


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
