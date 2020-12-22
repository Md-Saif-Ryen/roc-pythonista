def largest_even(lst):
    if max(lst) % 2 == 0:
        return max(lst)
    elif (max(lst) - 1) % 2 == 0:
        return max(lst) - 1
    else:
        pass


lst = [3, 9, 5, 8, 4, 7, 3, 6, 6]
print(largest_even(lst))