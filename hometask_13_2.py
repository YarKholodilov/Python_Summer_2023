def palindrome_gen():
    n = 0
    while True:
        n += 1
        if str(n) == str(n)[::-1]:
            yield n


g = palindrome_gen()
for _ in range(int(input('введите целое число: '))):
    print(next(g), end=' ')