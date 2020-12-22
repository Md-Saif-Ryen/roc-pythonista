def grid(somelist):
    j = 0
    while j < 6:
        a = ""
        i = 0
        while i < len(somelist):
            a = a + str(somelist[i][j])
            i += 1
        print(a, end="\n")
        j += 1
    return a


Grid = [
    [".", ".", ".", ".", ".", "."],
    [".", "O", "O", ".", ".", "."],
    ["O", "O", "O", "O", ".", "."],
    ["O", "O", "O", "O", "O", "."],
    [".", "O", "O", "O", "O", "O"],
    ["O", "O", "O", "O", "O", "."],
    ["O", "O", "O", "O", ".", "."],
    [".", "O", "O", ".", ".", "."],
    [".", ".", ".", ".", ".", "."],
]

content = grid(Grid)