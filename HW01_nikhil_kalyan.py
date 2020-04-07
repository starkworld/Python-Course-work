""""Created on Sun Feb 4 17:57:57 2020

        @author: nkalyan🤠
         Implementing rock, Paper, Scissor game using simple approach"""



import random


#Code for player input choosing
def player_choice() -> str:
    player_input: str = input("Enter your choice,\n(rock/paper/scissor/Quit)?\n")
    player_input = player_input.lower()
    while player_input != ("rock" or "r") and player_input != ("paper" or "p") and player_input != ("scissor" or "s") and player_input != ("quit" or "q"):
        print(player_input, "??")
        player_input = input("That choice is not valid. Enter your choice (rock/paper/scissor/quit):")
    return player_input


#Code for computer input choosing
def computer_choice() -> str:
    computerInt: int = random.randint(0, 2)
    if computerInt == 0:
        computer = "rock"
    elif computerInt == 1:
        computer = "paper"
    elif computerInt == 2:
        computer = "scissor"
    else:
        computer = "What? Error Buddy!!"
    return computer


# Code of winner deciding
def winner_code() -> bool:
    player_input: str = player_choice()
    if player_input == "quit":
        return False
    computer_input: str = computer_choice()
    while player_input != "quit":
        if player_input == computer_input:
            print("It's a Tie!!\n"
                  "want to play again..?")
        elif player_input == "rock":
            if computer_input == "paper":
                print("You lost try again\n"
                      "Want to play again..?")
            else:
                print("Yeah!, You Win\n"
                      "Want to play again..?")
        elif player_input == "paper":
            if computer_input == "rock":
                print( "Yay!!, You win!\n"
                       "Want to play again..?")
            else :
                print("You lost..., Try again\n"
                      "Want to play again..?")
        elif player_input == "scissor":
            if computer_input == "rock" :
                print("You lost..., Try again\n"
                      "Want to play again..?")
            else:
                print("Yay, You win!\n"
                      "Want to play again..?")
        break
    #else:
     #   print("Thank you for playing")
    return True


#code of multiple games until player quits
def main() -> None:
    again: bool = True
    while again:
        again = winner_code()

    print("Thanks for Playing...")


if __name__ == "__main__":
    main()