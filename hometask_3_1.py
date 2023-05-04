salary = float(input("введите ЗП сотрудника, для расчета средней ЗП введите ноль " ))
salary_total = 0
count = 0
while salary != 0:
   salary_total += salary
   count += 1
   salary = int(input())

print(salary_total/count)