import itertools
banknotes = (50, 100, 200, 500, 1000, 5000)
res = set()
for i in range(1, 7):
    for x in itertools.combinations(banknotes, i):
        res.add(sum(x))
# print(*res, sep='\n')
answer = sorted(list(res))
print(*answer, sep='\n')
