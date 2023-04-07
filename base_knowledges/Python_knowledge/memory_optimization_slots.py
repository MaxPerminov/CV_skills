# Memory Optimization:
# Use __slots__ magic to force Python. This can save lots of memory
# and provide faster access to class attributes.

class Team:
    __slots__ = ["name", "score"]

    def __init__(self, name, score):
        self.name = name
        self.score = score


x = Team("Atletico Madrid", 4)
print(x.name, x.score, sep=" : ")
