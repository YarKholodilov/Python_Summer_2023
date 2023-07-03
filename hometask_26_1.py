def similarity(text1, text2):
    mini = ''
    maxi = ''
    res = ''

    if text1 != text2 and (text1.isalpha() is False or text2.isalpha() is False):
        return False
    if text1 == text2:
        return True

    if len(text1) > len(text2):
        mini, maxi = text2, text1
    elif len(text1) < len(text2):
        mini, maxi = text1, text2

    if mini in maxi and (len(maxi)-len(mini) == 1):
        return True
    else:
        for i in range(len(mini)):
            if maxi[i] == mini[i]:
                res += '*'
            else:
                res += maxi[i]

        if len(text1) == len(text2):
            for i in range(len(text1)):
                if text1[i] == text2[i]:
                    res += '*'
                else:
                    res += text1[i]

        if len(text2) - res.count('*') > 1 and (len(text1) == len(text2)):
            return False
        elif res != len(mini) * '*' and (len(text1) != len(text2)):
            return False
        else:
            return True



t1, t2 = 'qw', 'w'
print(similarity(t1, t2))