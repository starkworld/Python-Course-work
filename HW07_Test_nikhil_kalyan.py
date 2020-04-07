"""
Created on Monday 05 March 16:53:34 2020

@author: nkalyan🤠
        '''Testing Python Scripts using unittesting '''
"""

import unittest
from HW07_nikhil_kalyan import anagram_lst, anagram_dd, anagram_c, cover_alphabet, web_analyzer
from typing import List,Tuple, Set


class TestAnagramList(unittest.TestCase):
    """Testing anagram list method"""
    def test_anagram_lst(self):
        self.assertTrue(anagram_lst('dormitory', 'dirtyroom'))
        self.assertFalse(anagram_lst('Prof JR', 'Rj pro'))
        self.assertFalse('', '')
        self.assertTrue('Fried', 'Fired')
        self.assertTrue('rail safety', 'fairy tales')


class TestAnagramDefaultDict(unittest.TestCase):
    """Testing anagram dictionary method"""
    def test_anagram_dd(self):
        self.assertTrue(anagram_dd('School Master', 'The ClassRoom'))
        self.assertFalse(anagram_dd('listen', 'school'))
        self.assertTrue('debit card', 'bad credit')
        self.assertTrue('Coronavirus', 'Carnivorous')
        self.assertFalse('', '')


class TestAnagramCounter(unittest.TestCase):
    """Testing anagram counter method"""
    def test_anagram_c(self):
        self.assertTrue(anagram_c('The Eyes', 'They see'))
        self.assertFalse(anagram_c('Window', 'Willow'))
        self.assertFalse('', '')
        self.assertTrue('evil', 'vile')
        self.assertTrue('pat', 'tap')


class TestCoverAlphabet(unittest.TestCase):
    """Testing cover alphabet method"""
    def test_cover_alphabet(self):
        self.assertTrue(cover_alphabet("abcdefghijklmnopqrstuvwxyz"))
        self.assertTrue(cover_alphabet("aabbcdefghijklmnopqrstuvwxyzzabc"))
        self.assertTrue(cover_alphabet("The quick brown fox jumps over the lazy dog"))
        self.assertTrue(cover_alphabet("We promptly@!$ (judged) antique ivory buckles for the next prize"))
        self.assertFalse(cover_alphabet("12435gjhugbf!!#$((%)(("))
        self.assertFalse(cover_alphabet('nvhiowmgdj'))
        

class TestWebAnalyzer(unittest.TestCase):
    """Testing web analyzer method"""
    def test_web_analyzer(self):
        weblogs: List[Tuple[str, str]] = [
            ('Nanda', 'google.com'), ('Maha', 'google.com'),
            ('Fei', 'python.org'), ('Maha', 'google.com'),
            ('Fei', 'python.org'), ('Nanda', 'python.org'),
            ('Fei', 'dzone.com'), ('Nanda', 'google.com'),
            ('Maha', 'google.com'), ]

        summary: List[Tuple[str, List[str]]] = [
            ('dzone.com', ['Fei']),
            ('google.com', ['Maha', 'Nanda']),
            ('python.org', ['Fei', 'Nanda']), ]

        self.assertEqual(web_analyzer(weblogs), summary)
        
        
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
