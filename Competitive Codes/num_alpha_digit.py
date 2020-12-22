def count_all(txt):
    """gives you number of letters and digits in a string"""
    dic = {"LETTERS": 0, "DIGITS": 0}
    for i in txt:
        if i.isnumeric():
            dic["DIGITS"] += 1
        elif i.isalpha():
            dic["LETTERS"] += 1
        else:
            pass
    return dic


print(count_all("roc4 2y77g99"))