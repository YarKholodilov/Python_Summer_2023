def max_designer_number(lst):
    stroka = ''
    dig = {}     # словарь, ключ - номер позиции в списке
    rotated = sorted(lst, reverse=True)   # сортирую список по убыванию
    nlst = []           # список для значений в словарь dig
    for i in range(len(rotated)):
        nlst.append([])
        x = len(str(rotated[i]))
        if -9 <= rotated[i] <= 9:
            nlst[i].append(rotated[i])
            dig[i] = nlst[i]
        while x != 1:
            nlst[i].append(rotated[i] // (10 ** (x - 1)))
            x -= 1
            if x == 1:
                nlst[i].append(rotated[i] // (10 ** (x - 1)))
                dig[i] = nlst[i]
    final_dict = sorted(sorted(dig.values()), key=lambda x: (x[0], -len(x), x[-1]), reverse=True)  # последние значения список списков вставляем в строку

    for i in final_dict:
        stroka += str(i[-1])
    return stroka


# lst = [8, 9, 7, 25]
lst = [99, 2, 919, 9, 5, 92, 127, 3000]
print((max_designer_number(lst)))
