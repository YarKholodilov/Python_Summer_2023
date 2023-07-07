def invertions_num(lst):
    count = 0
    for i in range(1, len(lst)):
        for x in range(len(lst)-1):
            if lst[i] < lst[x] and i > x:
                count += 1
    return count


# lst = [1, 2, 3, 4, 5]
lst  = list(map(int, input('введите список чисел через пробел: ').split()))
print(invertions_num(lst))

