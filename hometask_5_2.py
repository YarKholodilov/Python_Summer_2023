n = int(input())
dividers = [1]
s_div = []
count = 0

for i in range(2, (n//2)+1):
    if n % i == 0:
        dividers.append(i)
dividers.append(n)
print("Все делители:")
print(*dividers)
print()

for x in dividers:
    for i in range(1, x+1):
        if x % i == 0:
            count += 1
    if count == 2 and x != 1:
        s_div.append(x)
    count = 0
print("Простые делители и их степени:")
# print(*s_div)


pows = dict()
pow_count = 0
for x in range(len(s_div)):
    while n % s_div[x] == 0:
        pow_count += 1
        n = n / s_div[x]
        # print(n, s_div[x], pow_count, n % s_div[x])
    pows[s_div[x]] = pow_count
    if n % s_div[x] != 0:
        pow_count = 1
    pow_count = 0


for k, v in pows.items():
    print(k, '-', v)
