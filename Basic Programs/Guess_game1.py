def Guess_games1():
    """Its a simple guessing game"""
    import random
    i = 1
    while i < 10:
        if i == 1:
            print("Hello...!!!")
            print("Welcome to the brand new Guessing Game...!!!")
            print(
                "My name is Cha.I am programmed to guide you in this game.\nPlease listen to my instructions very carefully.")
            print(
                "In this game,You are given nine chances to guess a number that I am thinking.\nIf you fail to do so within the given chances,You lose.")
            print(
                "Important : Number to be guessed is in the range (1, 30).\nIf you guess any number out of it,You will lose a guessing chance for not following my instructions.")
            print("And lastly,As per the number of chances you will use,I will rank you accordingly.")
            print("Good Luck..!!")
            cha_num = random.randint(1,30)
        print("You have", 10 - i, "chances left.")
        print("Please guess a number.")
        num = int(input())
        if num < cha_num and num >= 1:
            print("Hint : Guess a greater number.")
        elif num < 1:
            print("Out of range...!!!\nOne chance is taken for violating Cha's instructions")

        elif num == cha_num:
            print("Hurray...!!!\nYou guessed the right number.")
            print("You win...!!!")
            if i == 1:
                print("In just one chance....")
                print("You must be a cheater....\nKidding..!!!")
                print("You are ranked as 'Legend Predictor'")
            if i > 1 and i <= 3:
                print("You have used", i, "chances for guessing.")
                print("You are ranked as 'Pro Predictor'")
            if i > 3 and i < 7:
                print("You have used", i, "chances for guessing.")
                print("You are ranked as 'Nice Predictor'")
            if i >= 7 and i < 10:
                print("You have used", i, "chances for guessing.")
                print("You are ranked as 'Naive Predictor'")
            break
        elif num > cha_num and num <= 100:
            print("Hint : Guess a lesser number.")
        elif num > 100:
            print("Out of range...!!!\nOne chance is taken for violating Cha's instructions")
        i += 1
        if 10 - i == 0:
            print("Alas..!! but you have used all your 9 chance of guessing.\nAs per the rule,You lose.")
            print("Game Over")

def Guess_game2():
    """Another guessing game"""
    import random
    num = random.randint(1, 30)
    print("you got to guess a number between 1 and 30.\nAnd you will have 10 chances for that.\nGood Luck")
    i = 1
    while i <= 10:
        try:
            print("Take a guess")
            inp = int(input())
        except Exception as e:
            print("No alphabetical statement..!!")
            continue
        else:
            if inp < num:
                print("Guess a greater number.")
            elif inp > num:
                print("Guess a lesser number.")
            else:
                break
        i += 1
    if inp == num:
        print("you guess that right.")
        print("You have used " + str(i) + " chances to guess.")
    else:
        print("You lose.")

Guess_games1()