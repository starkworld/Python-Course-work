"""
Created on 22 Friday feb 16:53:34 2020

@author: nkalyan🤠
        Implementing test cases on Python Scripts on strings.
"""


def split_strings(string):
    """Split string into words as list"""
    splitter = string.split()
    return splitter


def combine_strings(splitter):
    """Combine words into a list"""
    combined: str = " ".join(splitter)
    return combined


def single_to_plural(string: str) -> str:
    """This function Convert singular to plural """
    for char in string:
        """Checks weather it is word or not"""
        if not char.isalpha():
            raise ValueError('You did not input a word. ')

    if string.endswith('y'):
        if string.endswith(('ay', 'ey', 'iy', 'oy', 'uy')):
            return string + 's'
        else:
            return string[:-1] + 'ies'

    if string[-1:] in 'osxz':
        return string + 'es'
    elif string[-2:] in ['ch', 'sh']:
        return string + 'es'

    return string + 's'


def main() -> None:
    """This calls the all the methods to run script"""
    string: str = input('Please enter some words/string: ')
    splitter = split_strings(string)
    try:
        for i in range(len(splitter)):
            splitter[i] = single_to_plural(splitter[i])
    except ValueError as e:
        print(e)

    string = combine_strings(splitter)
    print(string)


if __name__ == '__main__':
    main()
