n = int(input())
matrix = [[' '] * n for _ in range(n)]
num = 1
x, y = 0, 0
cycles = 0

for i in range(n-1):                           #заполняем спираль слева направо
    for y in range(cycles, n-cycles):
        if num <= n ** 2 and matrix[x][y] == ' ':
            if num <= 9:
                matrix[x][y] += str(num) + ' '
            else:
                matrix[x][y] += str(num)
            num += 1

    for x in range(cycles + 1, n-cycles):       #заполняем спираль сверху вниз
        if num <= n ** 2 and matrix[x][y] == ' ':
            if num <= 9:
                matrix[x][y] += str(num) + ' '
            else:
                matrix[x][y] += str(num)
            num += 1

    for y in range(-1-cycles, -n-1+cycles, -1):        #заполняем спираль справа налево
        if num <= n ** 2 and matrix[x][y] == ' ':
            if num <= 9:
                matrix[x][y] += str(num) + ' '
            else:
                matrix[x][y] += str(num)
            num += 1

    for x in range(-y - 1, -n + 1 + cycles, -1):            #заполняем спираль снизу вверх
        if num <= n ** 2 and matrix[x][y] == ' ':
            if num <= 9:
                matrix[x][y] += str(num) + ' '
            else:
                matrix[x][y] += str(num)
            num += 1
    x -= 1
    y -= 1
    cycles += 1

for row in matrix:
    print(*row)