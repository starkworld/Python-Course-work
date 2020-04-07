"""Created on Sun Feb 15 17:57:57 2020

        @author: nkalyan🤠
            Implementing a program for finding max of 3 numbers using user defined functions"""
import sys


def get_input(int):
    """This function Handles the exception"""
    while True:
        try:
            return float(input(int))
        except ValueError:
            print("Your Input cannot be strings")


def maxofthree(a, b, c):
    """"This Function represent simple algorithm which takes the 3 user inputs compare the 3 input values and
            return the maximum value"""
    if (a >= b) and (a >= c):
        largest = a
        print(f"Maximum of {a} {b} {c} is: {largest}")
        sys.exit ()
    elif (b >= a) and (b >= c):
        largest = b
        print(f"Maximum of {a} {b} {c} is: {largest}")
        sys.exit()
    else:
        largest = c
        print(f"Maximum of {a} {b} {c} is: {largest}")
        sys.exit()


def main() -> None:                                    # main Function which calls the maxofthree() to perform operations
    """"this is a general function that calls the
            appropriate functions to perform a given task and handles exception"""
    val1 = get_input("Enter Value of a: ")


    val2 = get_input("Enter value of b: ")
    val3 = get_input("Enter value of c: ")

    maxofthree(val1, val2, val3)                             # calls the function to perform the operation


if __name__ == "__main__":
    main()

