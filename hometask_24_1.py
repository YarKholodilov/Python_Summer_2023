"сортировка без встроенных функуий"

def my_sort(arr):
    flag = True
    while flag != False:
        flag = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                flag = True
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return f'Отсортированный по возрастанию список {arr}'


# lst = [101, 2, -1, -100, 5, 134, 43, 0, -75, 45, 99, 1, 2]
lst = list(map(float, input('введите список чисел через пробел: ').split()))
print(my_sort(lst))
