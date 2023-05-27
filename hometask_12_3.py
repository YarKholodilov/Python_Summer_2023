def list_conseq(conseq):
    res = []

    if conseq.count('-') - conseq.count(',') != 1:
        return 'введён неверный формат начальной строки'
    elif '-' in str(conseq):
        conseq = conseq.replace(' ', '').replace('-', ' ')
    else:
        return 'введён неверный формат начальной строки'

    stop_start = conseq.split(',')

    for i in range(len(stop_start)):
        indx = stop_start[i].index(' ')
        x = stop_start[i][:indx]
        y = stop_start[i][indx + 1:]
        if int(x) <= int(y):
            res += [num for num in range(int(x), int(y) + 1)]
        else:
            res += [num for num in range(int(y), int(x) + 1)]
        # total = [res[i] for i in range(len(res)-1)]
    return res


stroka = input("введите строку заданного формата 'ЧИСЛО-ЧИСЛО' через запятую: ")     #'1-2, 23-29, 3-1'
print(list_conseq(stroka))

