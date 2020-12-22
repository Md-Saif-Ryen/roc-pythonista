def factorial(num):
    """gives factorial of an input"""
    if num == 1:
        return num
    else:
        return num * factorial(num - 1)


while True:
    try:
        num1 = int(input())
        break
    except ValueError:
        print("Invalid input!")
        continue
print(factorial(num1))