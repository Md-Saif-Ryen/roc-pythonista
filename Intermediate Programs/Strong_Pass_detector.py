import re

def upper_check(password):
    if re.search("[A-Z]", password):
        return True
    return False


def lower_check(password):
    if re.search("[a-z]", password):
        return True
    return False

def digit_check(password):
    if re.search("[0-9]", password):
        return True
    return False



def other_check(password):
    if re.search("[!@#$%^&*.]", password):
        return True
    return False

# a = input()
# print(other_check(a))

def pass_checker():
    print("NOTE : Your password must contain 'A-Z', 'a-z', '0-9' and '!-*' with a length of atleast 8 characters.")
    name = input("Enter your name :")
    password = input("Enter your password :")
    if len(password)>=8 and upper_check(password) and lower_check(password) and digit_check(password) and other_check(password):
        return f"{name},your password is strong.!"
    else:
        return f"{name},your password is weak\nPlease try again"


print(pass_checker())