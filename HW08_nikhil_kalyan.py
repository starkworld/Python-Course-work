# coding=utf-8
"""
Created on Monday 05 March 16:53:34 2020

@author: nkalyan🤠
        '''implementing Python scripts of date time differences, reading files generator and analyzing file'''
"""

from datetime import datetime, timedelta
from typing import Tuple, Iterator, List, Any, TextIO, Dict, Union
import os
from prettytable import PrettyTable


def date_arithmetic() -> Tuple[datetime, datetime, int]:
    """Method that returns preferable operations that mentioned in assignment 8"""
    date1: str = "Feb 27, 2020"
    date2: str = "Feb 27, 2019"
    date3: str = "Feb 1, 2019"
    date4: str = "Sep 30, 2019"
    dt1: datetime = datetime.strptime(date1, '%b %d, %Y')
    dt2: datetime = datetime.strptime(date2, '%b %d, %Y')
    dt3: datetime = datetime.strptime(date3, '%b %d, %Y')
    dt4: datetime = datetime.strptime(date4, '%b %d, %Y')
    num_of_days = 3
    three_days_after_date_1: datetime = dt1 + timedelta(days=num_of_days)
    three_days_after_date_2: datetime = dt2 + timedelta(days=num_of_days)
    days_duration: int = (dt4 - dt3).days
    return three_days_after_date_1, three_days_after_date_2, days_duration


def file_reader(path: str, fields: int, sep: str = ',', header: bool = False) -> Iterator[Tuple[str]]:
    """ Generator that reads columns in the given file """
    try:
        fp: TextIO = open(path, "r")
    except FileNotFoundError:
        raise FileNotFoundError("File is not found!!!")
    else:
        with fp:
            for index, lines in enumerate(fp, 1):
                current_line: List[str] = lines.rstrip('\n').split(sep)
                if len(current_line) != fields:                  
                    raise ValueError(f"{fp} has {len(current_line)} on line {index + 1}and {fields} ")
                if not header or index != 1:
                    yield tuple(current_line)
            

class FileAnalyzer(object):
    """ Class to implement scanning files, printing files tables functions """

    def __init__(self, directory) -> None:
        """ Function to initializes directory """
        self.list_dictionary: Dict[str, Dict[str, int]] = dict()
        self.directory = directory
        self.files_summary: Dict[str, Dict[str, int]] = self.analyse_files()

    def analyse_files(self) -> Dict[str, Dict[str, int]]:
        """ Function to count number of lines, characters, functions and classes in a file """
        try:
            list_files: List[Union[str]] = os.listdir(self.directory)
        except FileExistsError:
            raise FileExistsError("FIle not exists in the directory please check it once!!!")
        else:
            for file in list_files:
                if file.endswith(".py"):
                    try:
                        fp: TextIO = open(os.path.join(self.directory, file), "r")
                    except FileNotFoundError:
                        raise FileNotFoundError("File is not found please enter valid path!!")
                    else:
                        with fp:
                            number_of_lines: int = 0
                            number_of_char: int = 0
                            number_of_func: int = 0
                            number_of_class: int = 0
                            file_name: str = file
                            for lines in fp:
                                number_of_lines += 1
                                number_of_char: int = number_of_char + len(lines)
                                lines: str = lines.strip()
                                if lines.startswith("def ") and (lines.endswith(":") or lines.endswith("")):
                                    number_of_func += 1
                                elif lines.startswith("class ") and (lines.endswith(":") or lines.endswith("")):
                                    number_of_class += 1
                        self.list_dictionary[file_name] = {"class": number_of_class, "function": number_of_func,
                                                           "line": number_of_lines,
                                                           "char": number_of_char}
        return self.list_dictionary

    def pretty_print(self) -> Iterator[Any]:
        """ Method that print the file summary in a pretty table"""
        pretty_table: PrettyTable = PrettyTable(
            field_names=["File Name", "Classes", "Functions", "Lines", "Characters"])

        for file_name in self.list_dictionary:
            pretty_table.add_row(
                [file_name, self.list_dictionary[file_name]["class"], self.list_dictionary[file_name]["function"],
                 self.list_dictionary[file_name]["line"], self.list_dictionary[file_name]["char"]])

        return pretty_table


def main() -> None:
    """Calls each methods, actually we dont require these function calling but better understanding we can write """
    print(date_arithmetic())
    try:
        for line in file_reader("Student_major", 1):
            print(line)
    except ValueError as e:
        print("You have entered wrong number of fields!!", e)
    p1 = FileAnalyzer('/Users/nikhilkalyan/PycharmProjects/SSW 810')
    print(p1.pretty_print())


if __name__ == "__main__":
    main()
