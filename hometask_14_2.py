def total(n):
    if n < 10:
        return n
    else:
        x = total(n // 10)
        # print(n//10 + n % 10)
        # print(n, n//10, n % 10)
        return x + n % 10

print(total(int(input('введите число: '))))




