# НАИМЕНЬШЕЕ ОБЩЕЕ КРАТНОЕ

print('введите список натуральных чисел lst = []')
lst = [1, 32, 4, 22]

def prime_dives(num):
    dev_simpl = dict()
    for i in range(2, num + 1):
        hm = 0
        while num % i == 0:
            hm += 1
            num //= i
        if hm:
            dev_simpl[i] = hm
        if num == 1:
            break
    return dev_simpl


nok_dict = dict()
for i in lst:
    d = prime_dives(i)
    for k, v in d.items():
        if nok_dict.get(k, 0) < v:
            nok_dict[k] = v


nok = 1
for k, v in nok_dict.items():
    nok *= (k ** v)
print(nok)

