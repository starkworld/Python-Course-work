"""
Created on Monday 29 feb 16:53:34 2020

@author: nkalyan🤠
        '''Implementing Python Scripts using lists '''
"""

from typing import Any, List, Optional


def list_copy(lst: List[Any]) -> List[Any]:
    """Copy the given list and returns new copied list"""

    new_list = [each_element for each_element in lst]
    return new_list


def list_intersect(list_1: List[Any], list_2: List[Any]) -> List[Any]:
    """Checks the two lists lst1 and lst2,
            return the new list with common elements in list1 & list2 """

    inter_list = [common_values for common_values in list_1 if common_values in list_2]
    return inter_list


def list_difference(list_1: List[Any], list_2: List[Any]) -> List[Any]:
    """ This Function that takes two lists as  parameters
        and returns a new list with the values that are  in l1, but NOT in l2"""

    differ_list = [values for values in list_1 if values not in list_2]
    return differ_list


def remove_vowels(string: str) -> str:
    """"This function removes the words starts with vowels and returns new string"""

    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    return " ".join(word for word in string.split(' ') if not word.startswith(vowels))


def check_pwd(password: str) -> bool :
    """Checks the passwords on certain stipulations and returns the boolean value"""

    upper = [u_count for u_count in password if u_count.isupper()]
    lower = [l_count for l_count in password if l_count.islower()]

    if password[0].isdigit() and len(password) >= 4:
        if len(upper) < 2 or len(lower) < 1:
            return False
        else:
            return True
    else:
        return False

    """pw = ((len(password) >= 4) and ((len[char for char in password if isupper()]) >= 2) 
            and any(upper.islower() for char in password) and (password[0].isdigit()))"""


class Queue(object):
    """Create a queue and perform queue operations like
            insert, get next, waiting queue values"""
    def __init__(self):
        """initialize the queue object"""
        self.queue: List[str] = list()

    def add(self, name) -> None:
        """Add person into the queue"""
        self.queue.append(name)

    def get_next(self) -> Optional[str]:
        """return the name of next person return none if no one there in queue"""
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            return None

    def waiting(self) -> List[str]:
        """Return the waiting customer in queue"""
        return self.queue


class DonutQueue(object):
    """Handle customer arriving for donuts,
            customer may be vip or normal.
                Serve sll vip customer before standard customers."""

    def __init__(self) -> None:
        """create objects for two diffeent types of queue based on priority"""
        self.vip_queue: Queue = Queue()
        self.standard_queue: Queue = Queue()

    def arrive(self, name: str, vip: bool) -> None:
        """If the person is vip then it adds into vip queue else in normal queue"""
        if vip:
            self.vip_queue.add(name)
        else:
            self.standard_queue.add(name)

    def next_customer(self) -> Optional[str]:
        """Method for the returning next serving person in queue"""
        next_cust = self.vip_queue.get_next()
        if next_cust is None:
            next_cust = self.standard_queue.get_next()
        return next_cust

    def waiting(self) -> str:
        """Return the waiting list of customers in queue"""
        vips = self.vip_queue.waiting ()
        standards = self.standard_queue.waiting ()
        customer_queue_line = vips + standards
        return ", ".join(customer_queue_line)


def reorder(list_1: List[Any]) -> List[Any]:
    """This function takes a list and returns it in sorted order"""
    new_list: list = []

    for ele in list_1:
        new_list.append(ele)
        temp = new_list.index(ele)

        while temp > 0:
            if new_list[temp - 1] > new_list[temp]:
                new_list[temp - 1], new_list[temp] = new_list[temp], new_list[temp-1]
            else:
                break
            temp = temp - 1

    return new_list


def main() -> None:
    """Printing of the statements"""

    print(list_intersect([1, 2, 3], [1, 2, 4]))
    print(list_intersect([1, 2, 3], [4, 5, 6]))
    print(list_copy([2, 5, 0, -11, 22]))
    print(list_difference([1, 2, 3, 9, 55, 101], [2, 6, 8, 99, 201]))
    print(remove_vowels("My name is Prof JR"))
    print(check_pwd("003NickyY"))
    print(reorder([3, 5, 6, -4, 6, 9, 12, 3, 33]))

    my_queue = DonutQueue()
    print(my_queue.arrive('Prof JR', True))
    print(my_queue.arrive('Nanda', False))
    print(my_queue.next_customer())
    print(my_queue.waiting())


if __name__ == '__main__':
    main()
