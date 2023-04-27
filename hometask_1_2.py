print("Пожалуйста, введите два целых цисла:")
x, y = int(input()), int(input())

bigger = (x + y)

if (x - y) > bigger:
    bigger = (x - y)
if (x * y) > bigger:
    bigger = (x * y)
if (x / y) > bigger:
    bigger = (x / y)
if (x // y) > bigger:
    bigger = (x // y)

print(bigger)

# проверки:
# print()
# print(x + y)
# print(x - y)
# print(x * y)
# print(x / y)
# print(x // y)
