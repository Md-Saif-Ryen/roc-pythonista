class ones_threes_nines:
    """gives number of nines threes and ones that an integet is consist of"""

    def __init__(self, number):
        self.answer = f"nines:{number//9}, threes:{number%9//3}, ones:{number%9%3}"
