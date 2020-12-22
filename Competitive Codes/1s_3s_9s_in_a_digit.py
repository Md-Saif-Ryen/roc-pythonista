class ones_threes_nines:
    """gives number of nines threes and ones that an integet is consist of"""
#For example----
#if you enter 20,it will print--
#nines:2, threes:0, ones:2

    def __init__(self, number):
        self.answer = f"nines:{number//9}, threes:{number%9//3}, ones:{number%9%3}"
