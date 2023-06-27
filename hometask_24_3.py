" Функция на определение закрытых скобок () "
def valid_braces(data):
    res = 0
    for i in range(len(data)):
        if data[i] == '(':
            res += 1
        elif data[i] == ')':
            res -= 1
            if res < 0:
                return False
    if res > 0:
        return False
    else:
        return True


data = input('введите строку со скобками: ')
print(valid_braces(data))
