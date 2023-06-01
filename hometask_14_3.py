def tri_2(n):
    print('*'* n, end='')
    print()
    n -= 1
    if n > 1:
        tri_2(n)
    print('*' * n, end='')
    print()


n = int(input('введите целое число: '))
print()
tri_2(n)
print('*' * n)


