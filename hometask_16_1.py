import re
n = int(input('введите двузначное число, с которым будем сравнивать: '))
x = input('введите другое число: ')
template = re.findall(r'\b\d{1,2}\b', x)
for i in template:
    if 0 < int(i) < n:
        print(int(i))

