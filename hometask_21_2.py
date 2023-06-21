def find_min_way(mtx):
    n, m = len(mtx), len(mtx[0])   # размерность матрицы N - строки, M - столбцы
    res = [[0] * m for i in range(n)] # создаем аналог исходной матрицы, в которую будем заполнять значения суммирования предыдущих клеток

    for i in range(0, n):
        for j in range(0, m):
            res[i][j] = mtx[i][j]
            res[i][j] += min(res[i][j - 1], res[i - 1][j])
    return(res[n-1][m-1] + res[0][0])


mtx = [[10, 20, 10], [5, 1, 50], [50, 64, 50]]
print(find_min_way(mtx))