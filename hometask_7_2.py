def code(string, n):
    shift = n % 26
    res = ''
    for i in string:
        if i.isalpha():
            if i.isupper():
                if ord(i) + shift > ord('Z'):
                    res += chr((ord(i) + shift) - 26)
                else:
                    res += chr((ord(i) + shift))
            elif i.islower():
                if ord(i) + shift > ord('z'):
                    res += chr((ord(i) + shift) - 26)
                else:
                    res += chr((ord(i) + shift))
        else:
            res += i
    return res


print(code(input('введите текст для шифрования на английском: ').lstrip(), int(input('введите число сдвигов: '))))
