def sequence_gen():
    n = 0
    while True:
        n += 1
        yield n if n % 2 else -n


g = sequence_gen()
for _ in range(int(input('введите целое число: '))):
    print(next(g), end=', ')
