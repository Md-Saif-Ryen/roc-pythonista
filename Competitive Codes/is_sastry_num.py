def sastry_number(n):
    num = str(n) + str(n + 1)
    print(num)
    sqrt = int((num)) ** 0.5
    print(sqrt)
    print(round(sqrt))
    if round(sqrt) - sqrt == 0:
        return True
    else:
        return False