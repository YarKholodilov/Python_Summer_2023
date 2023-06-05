dct = {1: 1, 2: 2, 3: {2: 22, 3: {1: 111, 2: 222, 3: {0: 111, 1: 2222, 2: 333333}}, 1: 11}, 4: 22, 5: 55}
def find_key(d, x):
    lst = []
    if x in d:
        lst.append(d[x])
    for k, v in d.items():
        if type(v) == dict:
            lst.append(find_key(v, x))
    return lst

def flat(lst):
    if not lst:
        return []
    if isinstance(lst[0], list):
        return flat(lst[0]) + flat(lst[1:])
    return lst[:1] + flat(lst[1:])


print(flat(find_key(dct, 1)))

