import math

class Fibonacci:
    def __init__(self):
        self.x = 0
        self.y = 1
        self.limit = math.inf
    def __iter__(self):
        return self
    def __next__(self):
        if self.x > self.limit:
            raise StopIteration
        self.x, self.y = self.y, self.x + self.y
        return self.x


fibonacci = Fibonacci()
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))



