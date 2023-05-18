lst = list(input())

#lst = [[1, 5, 3], [2, 44, 111, 4], [35143], [0]]

for i in lst:
    i.sort(reverse=True)

def count_digit(spis):
    t = ''
    for i in spis:
        t += str(i)
    return len(t)

spisok =(sorted(lst, key=lambda x: count_digit(x)))
print(spisok)

