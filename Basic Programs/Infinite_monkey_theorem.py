"""
1, import random
2, user input
3, function to generate a random string of same length as user input.
4, function to compare the randomly generated string to the user's string and giving it a score each time it generates and compare.
"""

import random

def random_str(user_str):
    """This function will produce a random string of same lenght as the user Enter"""
    gen_str = ''
    char = ' abcdefghijklmnopqrstuvwxyz'
    for i in range(len(user_str)):
        cha = char[random.randrange(27)]
        gen_str += cha
    return gen_str

def check_str(user_str, gen_str):
    """This function will make sure if the generated string is equal to user string or not"""
    if user_str.lower() == gen_str:
        return True
    return False



def main(user_str):
    """This function runs the above two funcitons and return the number of times
    that monkey hit the keyboard to randomly get the user string"""
    scr = 0
    while True:
        gen_str = random_str(user_str)
        # print(f'{gen_str} ---->> Monkey hitting key-board >>> {scr} times')
        if check_str(user_str, gen_str):
            scr += 1
            break
        else:
            scr += 1 
            continue
    return f'Monkey hit the key-board {scr} times to enter your input.'


inp = input('Enter here --->>> ')
print(main(inp))