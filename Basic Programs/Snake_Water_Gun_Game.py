# Snake > Water
# Gun < Water
# Gun > Snake
# import random
import random

def S_W_G1():
    print("Please enter the user name.")
    name = input()
    char = ["snake", "water", "gun"]  # list of characters
    i = 0
    score_com = 0
    score_user = 0
    while i < 10:
        cha = random.choice(char)
        print("Please choose a character.")
        man = input()
        print("Computer's choosen character is", cha)
        if cha == "snake":
            if man == "water":
                score_com += 10
            if man == "gun":
                score_user += 10
        elif cha == "water":
            if man == "snake":
                score_user += 10
            elif man == "gun":
                score_com += 10
        elif cha == "gun":
            if man == "water":
                score_user += 10
            elif man == "snake":
                score_com += 10

        i += 1

    print("Score of Computer is " + str(score_com))
    print("Score of " + name + " is " + str(score_user))
    if score_com > score_user:
        print("Cha win this game.")
    elif score_user > score_com:
        print(name + " win this game.")
    else:
        print("This match is drawn.")
S_W_G1()