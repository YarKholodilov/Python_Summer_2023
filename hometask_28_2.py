# решение не в одну строчку.

def diff_num(stroka1, stroka2):
    count = abs(len(stroka1) - len(stroka2))

    if len(stroka1) >= len(stroka2):
        bigger, less = stroka1, stroka2
    else:
        bigger, less = stroka2, stroka1

    for i in range(len(less)):
        if less[i] != bigger[i]:
            count += 1
    return count


s1, s2 = map(str, input('введите два слова через пробел: ').split())
print(diff_num(s1, s2))
