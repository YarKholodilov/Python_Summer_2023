lst = [1, 1, 1, 1, 10, 1, 1, 1, 1, 1, 1, 1]

if len(lst) > 2:
    for i in lst:
        if lst.count(i) == 1:
            print(i)
elif len(lst) == 2 and lst[0] != lst[1]:
    print('2 different numbers')
else:
    print('in the list only one number or this an empty list')
