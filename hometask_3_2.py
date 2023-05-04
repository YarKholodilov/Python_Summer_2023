n = int(input('введите целое число: '))
digit = str(n)
for i in range(10):
   finder = digit.count(str(i))
   print(i, '-', finder)