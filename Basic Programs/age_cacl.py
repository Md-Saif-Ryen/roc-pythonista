print("Welcome to the 'Age Calculator'")
print("Rules are :\n1.Please follow the instructions.\n2.Please enter only in numerical format.")
while True:
    try:
        print("Enter your 'Year Of Birth'")
        yob = int(input())
        if yob < 1900:
            print("Out of range.!")
            continue
        else:
            break
    except Exception as e:
        print("Please follow the rules.")

while True:
    try:
        print("Enter your 'Month Of Birth'")
        mob = int(input())
        if mob < 1 or mob > 12:
            print("Out of range.!")
        else:
            break
    except Exception as e:
        print("Please follow the rules.")

while True:
    try:
        print("Enter your 'Day Of Birth'")
        dob = int(input())
    #did this to make sure that in months with 31 days user won't 
    #enter 31+ and in months of 30 days,user won't enter 30+ 
     #likewise in all cases!
        if mob == 1 or mob == 3 or mob == 5 or mob == 7 or mob == 8 or mob == 10 or mob == 12:
            if dob<1 or dob>31:
                print("Out of range.!")
                continue
            else:
                break
        elif (yob - 2000) // 4 == 0:
            if dob <1 or dob > 29:
                print("Out of range.!")
                continue
            else:
                break
      ##for leap years! 
     # year 2000 is a leap year so every 4 year after it
     # is also a leap year
    #here,if not leap year is concerned..
        elif (yob - 2000) // 4 != 0:
            if dob < 1 or dob > 28:
                print("Out of range.!")
                continue
            else:
                break
        elif mob == 4 or mob == 6 or mob == 9 or mob == 11:
            if dob <1 or dob>30:
                print("Out of range.!")
                continue
            else:
                break
    except Exception as e:
        print("Please follow the rules.")

while True:
    try:
        print("Enter the year,You wish to know your 'Age' in.")
        wyr = int(input())
        break
    except Exception as e:
        print("Please follow the rules.")
        continue
#calculating age with fun!
if (wyr - yob) < 0:
    print("Lmao,You have not been born yet.!")
elif (wyr - yob) == 0:
    print("Congrats,You have just been born.!")
else:
    print(f"Your age in {wyr} will be {wyr - yob} years.")








