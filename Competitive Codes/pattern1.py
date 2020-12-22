def grid(somelist):
    '''by using nested loop for list of lists
It creates pattern in the list'''
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
#returns
#..00.00..
#.0000000.
#.0000000.
#..00000..
#...000...
#....0....
