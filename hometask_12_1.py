def min_max_indexes(x):
    if len(x) == 0:
        return 'список пуст'
    ma = max(x)
    mi = min(x)
    res_ma = []
    res_mi = []
    flag = 1
    for i in range(len(x)):
        if len(set(x)) == 1:
            flag = 0
        if x[i] == ma:
            res_ma.append(i)
        elif x[i] == mi:
            res_mi.append(i)
    if flag == 0:
        return 'список содержит одиннаковые значения'
    else:
        return f'{res_mi} {res_ma}'


lst = [float(i) for i in input('Введите список чисел через пробел ').split()]
print(min_max_indexes(lst))          # вывод индекса минимального значения и индекса максимального значения