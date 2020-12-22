# ------------Shiritori Game-------------
"""
1.rule number 1====The first letter of second word must match the
  last letter of first word.
2.rule number 2====No word should be repeated.
"""


class Shiritori:
    def __init__(self):
        self.words = []
        self.game_over = False

    def play(self, word):
        self.word = word
        if len(self.words) == 0:
            self.words.append(self.word)
            return self.words
        elif self.word[0] == self.words[-1][-1]:
            self.words.append(self.word)
            return self.words
        else:
            self.game_over = True
            return "game over"

    def resart(self):
        self.words.clear()
        self.game_over = False
        return "game restarted"
