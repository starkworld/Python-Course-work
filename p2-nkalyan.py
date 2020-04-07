"""Created on Sun Feb 3 2020, 15:19:45

        @author: nkalyan🤠
        Implementing Python Script that asks user for a quiz score and convert
            that numeric score to grade"""


def grade_converter() -> bool:
    """"This function ask the user for input value,
            if it's a string then it convert to integer and catches an exception and
                then convert user input to grades and returns result"""

    while True:                                                         #simple Code for Catching exceptions
        try:
            score: str = input("Enter the quiz score: ")
            quiz_score: float = float(score)
            break
        except ValueError:
            print(f"Input is not a number" )
            return True

    while 0 <= quiz_score <= 100:                  #simple algorithm that convert scores to grade and return output
        if quiz_score >= 93:
            print("Your Grade is: A")
        elif 90 <= quiz_score < 93:
            print("Your Grade is: A-")
        elif 87 <= quiz_score < 90:
            print("Your Grade is: B+")
        elif 83 <= quiz_score < 87:
            print("Your Grade is: B")
        elif 80 <= quiz_score < 83:
            print("Your Grade is: B-")
        elif 70 <= quiz_score < 80:
            print("Your Grade is: C")
        else:
            print("You are failed: F")
        break
    else:
        print("Your input is not valid please enter numbers in between 0 to 100!!")
    return True


def main() -> None:                         #main Funtion which calls the grade_converter() to perform operations
    """"this is a general function that calls the
            appropriate functions to perform a given task"""
    grade_converter()


if __name__ == "__main__":
    main()
