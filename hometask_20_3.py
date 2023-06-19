import itertools
class Seq:
    def __init__(self):
        self.alfabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        self.numbers = [i for i in range(1, 27)]
        self.res = [x for y in zip(self.numbers, self.alfabet) for x in y]
        self.loop = itertools.cycle(itertools.chain(self.res))

    def __iter__(self):
        return self

    def __next__(self):
        for i in self.loop:
            return i


a = Seq()
for _ in range(115):
    lst = next(a)
    print(lst, end=', ')
