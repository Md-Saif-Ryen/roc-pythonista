def sum_fraction(lst):
    """Gives sum of fraction where num is first el of sublist and den is second"""
    x = 0
    for i in range(len(lst)):
        x += lst[i][0] / lst[i][1]
    return x


# Example
print(sum_fraction([[1, 2], [2, 5]]))
