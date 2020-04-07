"""
Created on Monday 05 March 16:53:34 2020

@author: nkalyan🤠
        '''Writing Python scripts on lists, dictionaries and sets'''
"""
from collections import defaultdict, Counter
from typing import List, Tuple, DefaultDict
import string


def anagram_lst(str1: str, str2: str) -> bool:
    """Method for anagrams using list"""
    list1, list2 = list(str1.lower()), list(str2.lower())
    return sorted(list1) == sorted(list2)


def anagram_dd(str1: str, str2: str) -> bool:
    """Anagram using default dictionaries"""
    def_dict: DefaultDict[str] = defaultdict(int)
    for char in str1.lower():
        def_dict[char] += 1
    for char in str2.lower():
        def_dict[char] -= 1
    
    return not any(def_dict.values())


def anagram_c(str1: str, str2: str) -> bool:
    """Implementing anagrams script using counters"""
    return Counter(str1.lower()) == Counter(str2.lower())


def cover_alphabet(sentence: str) -> bool:
    """Method that returns true if it covers all alphabet at least once otherwise false"""
    alphabet = set(string.ascii_lowercase)
    return set(sentence.lower()) >= alphabet


def web_analyzer(web_logs: List[Tuple[str, str]]) -> List[Tuple[str, List[str]]]:
    """Method that returns the web log of employers"""
    emp_dict: DefaultDict[str, set] = defaultdict(set)
    for employee, website in web_logs:
        emp_dict[website].add(employee)

    return [(website, sorted(emp_dict[website])) for website in sorted(emp_dict.keys())]


def main() -> None:
    """Calls the method to perform some operations"""
    str1 = 'dormitory'
    str2 = 'dirtyroom'
    print(anagram_lst(str1, str2))
    print(anagram_dd(str1, str2))
    print(anagram_c(str1, str2))
    print(cover_alphabet("abchQkkfv"))
    print(cover_alphabet('ABCDefghijklmnopqrstuvwxyZ'))


if __name__ == '__main__':
    main()

