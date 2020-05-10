"""
Created on Monday 24 feb 04:53:34 2020

@author: nkalyan🤠
        '''Implementing Python Scripts on strings and file '''
"""

from typing import Iterator


def reverse_string(string: str) -> str:
    """This function reverse the given string and returns it"""
    new_string: str = ''

    for each_character in string:
        new_string = each_character + new_string
    return new_string


def sub_string(target_string: str, string: str) -> int:
    first_index_value: int = 0
    last_index_value: int = 0

    if len(string) < len(target_string):
        raise IndexError("String index is out of range")

    while first_index_value < len(string):

        if string[first_index_value + last_index_value].lower() != target_string[last_index_value].lower():
            first_index_value += 1
            last_index_value = 0
            continue

        last_index_value += 1

        if last_index_value == len(target_string):
            return first_index_value
    return -1


def find_second(target_string: str, string: str) -> int:
    """ returns the offset of the second occurrence of Target in string2.
    Return -1 if Target does not occur twice in string2."""

    first_index: int = string.find(target_string, string.find(target_string) + 1)
    if first_index == -1:
        return -1
    else:
        return first_index


def get_lines(path: str) -> Iterator[str]:
    """Generator open a file for reading and open a file for each time"""

    try:
        """Handles the file not found exception if file is not found in directory/given path"""
        fp = open(path, 'r')

    except FileNotFoundError:
        print("File is not found!")

    else:
        with fp:

            for line in fp:
                line = line[:-1]
                while line.endswith('\\'):
                    line = line.rstrip('\\') + fp.readline().strip('\n')
                if not line.startswith('#'):



                    yield line.split('#')[0]


def main():
    """The main method is going to call the all the methods we have returned above"""

    string: str = input("Enter Your String: ")
    print("The Given string is reversed: ", reverse_string(string))

    str1: str = input("Enter your Target string: ")
    str2: str = input("Enter full String: ")
    print("The second string is found at starting index of: ", find_second(str1, str2))

    file_name = 'text1.txt'
    for line in get_lines(file_name):
        print(line)

    while True:
        try:
            tar: str = input ( "Enter Target string to find sub_string: ")
            print("The sub string is found at index of: ", sub_string(tar, string))
            break
        except IndexError as e:
            print("Index error!!", e)


if __name__ == '__main__':
    """""Calls the functions to perform operations"""
    main()

