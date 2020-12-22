"""
points to be noted::::
1.Road length must be specified.
2.Two player will play this game until one of them finishes the road and wins.
"""
import random as rd
from functools import reduce
import re


def check_input(inp):
    if re.search("[-]", inp):
        return False
    return True


def start_game():
    """This function starts the game after getting the info from the users."""
    player1 = []
    player2 = []
    i = 0
    j = 0
    while i <= length_of_road or j <= length_of_road:
        while True:
            print(f"Now {name1},Please press 'r' to roll the dice.")
            roll1 = input()
            if roll1 == "r":
                num1 = rd.randint(1, 6)
                player1.append(num1)
                i += num1
                print(f"You got {num1}")
                break
            else:
                print(f"{name1}, Please try again and press 'r' to roll the dice .")
                continue
        if i >= length_of_road:
            break
        while True:
            print(f"Now {name2}, Please press 'r' to roll the dice")
            roll2 = input()
            if roll2 == "r":
                num2 = rd.randint(1, 6)
                player2.append(num2)
                j += num2
                print(f"You got {num2}")
                break
            else:
                print(f"{name2}, Please try again and press 'r' to roll the dice .")
                continue
        if j >= length_of_road:
            break
    total_score1 = reduce(lambda x, y: x + y, player1)
    total_score2 = reduce(lambda x, y: x + y, player2)
    if total_score1 > total_score2:
        print(
            f"{name1}'s move-wise score list :{player1}\nTotal score is {total_score1}\nNumber of '6' :{player1.count(6)}"
        )
        print(
            f"{name2}'s move-wise score list :{player2}\nTotal score is {total_score2}\nNumber of '6' :{player2.count(6)}"
        )
        print(f"{name1} wins..!")
    elif total_score2 > total_score1:
        print(
            f"{name1}'s move-wise score list :{player1}\nTotal score is {total_score1}\nNumber of '6' :{player1.count(6)}"
        )
        print(
            f"{name2}'s move-wise score list :{player2}\nTotal score is {total_score2}\nNumber of '6' :{player2.count(6)}"
        )
        print(f"{name2}, wins..!")
    else:
        print(f"{name1} tied with {name2}")


print("DICE RACING GAME")
while True:
    """It takes the name of the players."""
    print("Please Enter player1's User name.")
    name1 = input()
    print("Please Enter player2's User name.")
    name2 = input()
    if name1.isalpha() and name2.isalpha():
        print(
            f"Hello..! {name1} and {name2}\n"
            f"I hope you players will enjoy your ride in this brand new 'Dice Racing Game'"
        )
        break
    else:
        print(
            "please enter a valid User's name(in one alphabetical word) and try again"
        )
        continue


while True:
    """Takes the length of the road of 'Dice Racing'"""
    try:
        print("Please enter the length of your road(length = around max. score)")
        length_of_road = int(input())
        if check_input(str(length_of_road)):
            break
        else:
            print("Invalid length")
            continue
    except ValueError:
        print("Length of your road must be a natural number.\nPlease try again.")
        continue


while True:
    print("Press 'Enter' to start the game")
    enter = input()
    if enter == "":
        start_game()
        break
    else:
        print("Please follow the instructions,and try again.")
        continue
