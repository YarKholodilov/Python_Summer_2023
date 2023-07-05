n = int(input('введите число от 1 до 18: '))

x = (n//2) + 1
mtx = [[1]*n for _ in range(n)]

for p in range(1, x):
    for i in range(p, len(mtx)-1):
        for j in range(p, len(mtx[i])-1):
            mtx[p][j] = p + 1
            if x > p > 1:
                mtx[-p][j] = p

for p in range(1, x):
    for i in range(p, len(mtx)-1):
        for j in range(p, len(mtx[i])-1):
            mtx[i][p] = p + 1
            if x > p > 1:
                mtx[i][-p] = p

for s in range(-2, -x, -1):
    for i in range(2, n+s):
        mtx[s][i] = s * -1

if n > 2:
    for g in range(0, x+1):
        mtx[-g-1] = mtx[g]


for i in mtx:
    print(i)