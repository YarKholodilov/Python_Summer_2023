import string, re
text = 'Напиши программу программу, которая устраняет повторение повторение слов, ' \
       'т.е. результат результат должен быть следующим: ' \
       'Напиши программу, которая устраняет повторение слов, ' \
       'т.е. результат результат должен быть следующим.'.replace(',', ' ,').replace(':', ' : ').replace('.', ' .')

words = text.split()
result_lst = []

for i in range(len(words)):
    if words[i] not in string.punctuation and words[i] not in result_lst:
        result_lst.append(words[i])
    elif words[i] in string.punctuation:
        if words[i] != ':':
            result_lst.append(words[i])
        else:
            break
res = ' '.join(map(str, result_lst)).replace(' , ', ', ').replace(' .', '.') + '.'

print(res)



