n, m = int(input('количество строк: ')), int(input('количество столбцов: '))
mtx = [[int(input('введите число и нажмите Enter: ')) for j in range(m)] for i in range(n)]
spisok = []

for i in mtx:
    for j in i:
        spisok.append(j)
spisok.sort(reverse=True)

print(spisok[:3])