# coding=utf-8
"""
Created on Monday 28 March 00:53:34 2020

@author: nkalyan🤠
        '''implementing Python scripts on'''
"""

from string import punctuation
from collections import defaultdict
import os


def get_line(path):
    """Method that get each line from the file and reads it"""
    
    try:        # Exception checker
        fp = open(path, 'r')
    
    except FileNotFoundError:
        print(f'Cannot open  {path} plz check. the path once')
    
    else:           # if exception does not occurs this block execute
        with fp:
            for line in fp:
                if line.strip(' \n\r') == '':
                    continue
                yield line.strip(' \n\r')


class ClassicBook(object):
    """
    A class that perform the main logic and which create the instance objects
    It's going to perform the all the major operations that required for this homework
    """

    def __init__(self):
        """A constructor that initialize the variables"""
        
        self.word_dictionary = defaultdict(int)
        self.character_freq_dictionary = defaultdict(int)
        self.path = str()
        self.words = list()

    def get_path(self, file_name='test.txt', path=os.getcwd()):
        """Method that writes path and read file"""
        self.path = os.path.join(path, file_name)

    def words_dictionary(self):
        """Method that return the words dictionary,
        Put each word in dictionary as its frequency occurs """
        
        lines = get_line(self.path)
        
        for line in lines:      # reads the each line
            translator = str.maketrans({key: ' ' for key in punctuation})
            string = line.translate(translator)
            for word in string.split(' '):
                word = word.strip()
                if word == '':
                    continue
                if word.isalpha():
                    self.word_dictionary[word.lower()] += 1

        return self.word_dictionary.items()

    def words_number_count(self):
        """Method that returns total word count"""
        num = 0
        for count in self.word_dictionary.values():
            num += count
        return '{:,}'.format(num)

    def distinct_words(self):
        """Method that return distinct words"""
        words_count = tuple(self.word_dictionary.keys())
        return '{:,}'.format(len(words_count))

    def top_25(self):
        """Method that return top 25 words in file"""
        self.words = sorted(self.word_dictionary.items(), key=lambda x: x[1], reverse=True)
        return self.words[:25]

    def sorted(self):
        """Method that perform sorting list of the each char occurrence in file"""
        
        for word in self.word_dictionary.keys():
            for cha in word:
                self.character_freq_dictionary[cha] += 1
        self.character_freq_dictionary = sorted(self.character_freq_dictionary.items(), key=lambda x: x[1], reverse=True)
        return self.character_freq_dictionary


def main():
    tom_sawyer = ClassicBook()
    tom_sawyer.get_path(file_name='TomSawyer.txt', path='/Users/nikhilkalyan/PycharmProjects/SSW 540')
    tom_sawyer.words_dictionary()
    print("Total Number of words in file are: ", tom_sawyer.words_number_count())
    print("Total Number of distinct words are: ", tom_sawyer.distinct_words())
    print(f"Top 25 words as apperared are:\n {tom_sawyer.top_25()}")
    print(f"Each Character frequency in sorted order is:\n {tom_sawyer.sorted()}")


if __name__ == '__main__':
    main()
