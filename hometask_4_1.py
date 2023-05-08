# решение 1
# print(eval(input()))



# решение 2
virazhenie = input().split()
if virazhenie[2] == '0' and (virazhenie[1] == '/' or virazhenie[1] == '//' or virazhenie[1] == '%'):
    print('на ноль делить нельзя')
    virazhenie = input().split()

x = int(virazhenie[0])
y = int(virazhenie[2])
operator = virazhenie[1]
result = 0

if operator == '+':
    result = x + y
elif operator == '-':
    result = x - y
elif operator == '*':
    result = x * y
elif operator == '/':
    result = x / y
elif operator == '//':
    result = x // y
elif operator == '%':
    result = x % y
elif operator == '**':
    result = x ** y

print(result)
