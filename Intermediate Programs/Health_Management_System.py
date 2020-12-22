def get_time():
    import datetime
    return datetime.datetime.now()
def log_file(name):
    print("What do you wish to log?")
    while True:
        print("Please press 'a' for exercise or 'b' for diet.\nPress here.")
        wish_1 = input()
        if wish_1 == "a":
            log_file_ex = open(name + "_Ex.txt", "a")
            print("Please log here.")
            log_file_ex.write("[" + str(get_time()) + "]" + " : " + input() + "\n")
            log_file_ex.close()
            print("You logged successfully.")
            print("Press 'a' to log more or 'b' to exit.\nPress here.")
            wish_2 = input()
            if wish_2 == "a":
                continue
            elif wish_2 == "b":
                break
        elif wish_1 == "b":
            log_file_di = open(name + "_Di.txt", "a")
            print("Please log here.")
            log_file_di.write("[" + str(get_time()) + "]" + " : " + input() + "\n")
            log_file_di.close()
            print("You logged successfully.")
            print("Press 'a' to log more or 'b' to exit.\nPress here.")
            wish_2 = input()
            if wish_2 == "a":
                continue
            else:
                break
def retrieve_file(name):
    print("What do you wish to retrieve?")
    while True:
        print("Please press 'a' for exercise or 'b' for diet.\nPress here.")
        wish_3 = input()
        if wish_3 == "a":
            try:
                retrieve_file_ex = open(name + "_Ex.txt")
                print(retrieve_file_ex.read())
                retrieve_file_ex.close()
                print("You retrieved successfully.\nYou may also retrieve 'diet'(If you have already logged).")
                print("Please press 'a' to do so or 'b' to exit.\nPress here.")
                wish_4 = input()
                if wish_4 == "a":
                    continue
                elif wish_4 == "b":
                    break
            except Exception as e:
                # print(e)
                print("No username found..!\nPlease Enter the correct name or try logging in.")
                break

        elif wish_3 == "b":
            try:
                retrieve_file_di = open(name + "_Di.txt")
                print(retrieve_file_di.read())
                print("You retrieved successfully.\nYou may also retrieve 'exercise'(If you have already logged).")
                print("Please press 'a' to do so or 'b to exit.\nPress here.")
                wish_4 = input()
                if wish_4 == "a":
                    continue
                elif wish_4 == "b":
                    break
            except Exception as e:
                # print(e)
                print("No username found..!!\nPlease Enter the correct name or try logging in.")
                break



print("Please Enter the user name.\nEnter here.")
name = input()
print("You wish to 'Log' or 'Retrieve'?\nPlease press 'a' to log or 'b' to retrieve.\nPress here.")
wish = input()
if wish == "a":
    log_file(name)
elif wish == "b":
    retrieve_file(name)