print("Пожалуйста, введите два целых цисла:")
x, y = int(input()), int(input())

if y == 0:
    print("Введите число не равное нулю:")
    y = int(input())

less_max = -100000 * ((x + y)**2)  # гарантированнно минимальное число
bigger = (x + y) #  присваиваем максимальной переменной первое возможное значение

# взял алгорит поиска максимального значения из предыдущего задания
if (x - y) > bigger:
    bigger = (x - y)
if (x * y) > bigger:
    bigger = (x * y)
if (x / y) > bigger:
    bigger = (x / y)
if (x // y) > bigger:
    bigger = (x // y)

# ищу второе наибольшее значение после максимального
if bigger > (x + y) > less_max:
    less_max = (x + y)
if bigger > (x - y) > less_max:
    less_max = (x - y)
if bigger > (x * y) > less_max:
    less_max = (x * y)
if bigger > (x / y) > less_max:
    less_max = (x / y)
if bigger > (x // y) > less_max:
    less_max = (x // y)

print(less_max)

#проверки:
# print()
# print(bigger, less_max)
# print(x + y)
# print(x - y)
# print(x * y)
# print(x / y)
# print(x // y)
