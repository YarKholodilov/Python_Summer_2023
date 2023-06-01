n = int(input('введите число: '))
count = 0
def num_num(n):
    global count
    count += 1
    if n < 10:
        return 1
    else:
        num_num(n//10)
        return count

print(num_num(n))
