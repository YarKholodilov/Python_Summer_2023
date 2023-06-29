lst = [1, 5, 6, 7, 9, 10]
res = []

for i in range(len(lst)-1):
    if lst[i] + 1 != lst[i+1]:
        res.append(lst[i+1])

if lst[0] + 1 != lst[1]:
    res.insert(0, lst[0])

print(res)