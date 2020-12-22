# Collatz Sequence -->> It states that for any natural number taken,dividing it by 2 if it is even and, multiplying it
#  by 3 and adding 1 ,if it is odd, then after certain steps we will get '1' no matter how big the number we take.
def coll(num):
    """This function will return a number depending if the input number is odd or even"""
    if num // 2 == 0:
        return num // 2
    else:
        return 3 * num + 1


while True:
    try:
        inp = int(input("Enter Number ----> "))
        break

    except ValueError:
        print("Please enter a Natural Number and try again.")
        continue

while True:
    result = coll(inp)
    if result == 1:
        break
    else:
        inp = result
        continue