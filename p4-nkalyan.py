"""Created on Sun Feb 17 2020, 12:19:45

        @author: nkalyan🤠
        Implementing Python script named guess number in which user has to guess the number in between 1 to 20
                using 6 guess tries."""
from random import randint


def get_input(int):
    while True:
        try:
            return float(input(int))
        except ValueError:
            print("Strings cannot be your guess")


def guess_number(name):
    """User defined function which performs the all the operations and prints the result"""
    guess_limit = 0
    magic_number = randint(1, 20)

    while guess_limit < 6:                              # perform the multiple guess operations and print output
        user_guess = get_input("Take a guess: ")
        if 0 < user_guess <= 20:                      # condition that allows the numbers only if in between 1 to 20
            guess_limit += 1
            if user_guess == magic_number:
                print(f"Good job, {name}! You guessed my number in {guess_limit} guesses!")
                break
            elif user_guess < magic_number:
                print("Your Guess is too low")
            elif user_guess > magic_number:
                print("Your Guess is too high")
        else:
            print("Try again, Your number must have be in the range of 1 to 20!!")
    else:
        print(f"The number I was thinking of was {magic_number}")
    return 0


def main() -> None:
    """Calls the guess number functions"""
    name1: str = input("Hello! What is your name?: ")
    print(f"Well, {name1}, I am thinking of a number between 1 and 20")
    guess_number(name1)


if __name__ == "__main__":
    main()
