def sequence_gen(lst):
    for i in lst:
        if i % 2:
            yield i

x = list(map(int, input('введите список целых чисел через пробел: ').split()))
g = sequence_gen(x)
for k in x:
    try:
        print(next(g), end=' ')
    except StopIteration:
        print('')
        break