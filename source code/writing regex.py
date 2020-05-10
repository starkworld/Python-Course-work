# coding=utf-8
"""
Created on Monday 28 March 00:53:34 2020

@author: nkalyan🤠
        '''implementing Python scripts on Regex'''
"""

import re
from typing import TextIO, List


def average(items: str):
    """custom method that calculates the average by taking an array as an input, and
        divides the sum of the array by the number of items in the array."""
    return sum(items) / len(items)


try:
    '''prompts the user for the filename, with error handling.'''
    file_name: str = input('Enter the file name (include path if file is outside directory): ')
except EOFError:
    print('EOF command given. Quitting...bye!')
    exit()
except ValueError:
    print('This input is invalid! Please try again.')
    exit()


try:
    """attemps to the open the file, with exception handling if the program
            cannot find the file or another error occurs."""
    file: TextIO = open(file_name)    
except FileNotFoundError:
    print('File cannot be opened:', file_name)
    exit()
except ValueError:
    print('An error occurred opening this file! Please try again.')
    exit()

items: List = []

try:
    """reads the file line by line"""
    for line in file:
        line: str = line.rstrip()                                    # strips the tailing characters

        matches: List[str] = re.findall('^New Revision: ([0-9]+.[0-9]+)', line)
                                            
        if len(matches) > 0:
            for item in matches:
                number: float = float(item)
                items.append(number)
except DeprecationWarning:
    print('Bad data was detected! Please check your file and try again.')
    exit()


if len(items) == 0:             # Make sure the program found at least 1 matching line before proceeding.
    print('The program did not find any matching lines! Please check your file and try again.')
    exit()

average = average(items)        # calls the average method and then rounds it to a single decimal place.
average = round(average, 1)


print(f'Average = {average}')
print(f'Number of lines = {len(items)}')
