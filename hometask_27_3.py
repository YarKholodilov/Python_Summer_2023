def ElementCounter(obj, count=0):
    if len(obj) == []:
        return 0
    for i in obj:
        count += 1
        if type(i) == list:
            return ElementCounter(i, count)
    return count


obj = [1, 2, 3, [4, 5]]
print(ElementCounter(obj))

