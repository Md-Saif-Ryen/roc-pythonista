def Guess_game2():
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
