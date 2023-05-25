import csv, openpyxl

columns = ['number', 'second_name', 'first_name', 'company', 'salary']
data = [[1,	'Егоров','Андрей','Семафор', 100], [2, 'Сидоров', 'Илья','ПАМ-ПАМ', 200], [3, 'Петров','Антон','НЕ-ПАМ', 130],
        [4, 'Петров', 'Артем','ПАМ-ПАМ', 150], [5, 'Смирнов', 'Александр','Газпродукт',500], [6, 'Бобров', 'Эльдар','Шестерочка', 50],
        [7, 'Пухов', 'Борис', 'ПАМ-ПАМ', 250], [8, 'Нечаев', 'Сергей', 'Шестерочка', 50], [9, 'Стругацкий', 'Борис', 'НИИ', 250],
        [10, 'Стругацкий', 'Аркадий', 'НИИ', 250]]

with open('hometask_11_2.csv', 'w', encoding='utf-8') as f1:
    writer = csv.writer(f1)
    writer.writerow(columns)
    for row in data:
        writer.writerow(row)

with open('hometask_11_2.csv', encoding='UTF-8') as f:
    rows = csv.DictReader(f)
    finished = sorted(rows, key=lambda x: (x['company'], x['second_name'], x['first_name']))


wb = openpyxl.Workbook()
wb.save('hometask_11_2.xlsx')

wb = openpyxl.load_workbook('hometask_11_2.xlsx')
ws = wb.active

row_name = []
for i in finished:
    for k in i.keys():
        if k not in row_name:
            row_name.append(k)
ws.append(row_name)

numbers = []
for i in finished:
    num = i['number']
    numbers.append(num)

surname = []
for i in finished:
    s = i['second_name']
    surname.append(s)

names = []
for i in finished:
    n = i['first_name']
    names.append(n)

companies = []
for i in finished:
    c = i['company']
    companies.append(c)

salary = []
for i in finished:
    zp = i['salary']
    salary.append(zp)


for i in range(1, len(numbers)+1):
    ws.cell(i+1, 1).value = int(numbers[i-1])

for i in range(1, len(surname)+1):
    ws.cell(i+1, 2).value = surname[i-1]

for i in range(1, len(names)+1):
    ws.cell(i+1, 3).value = names[i-1]

for i in range(1, len(companies)+1):
    ws.cell(i+1, 4).value = companies[i-1]
    ws.cell(len(companies)+2, 4).value = 'ИТОГО:'

for i in range(1, len(salary)+1):
    ws.cell(i+1, 5).value = int(salary[i-1])
    ws.cell(len(salary) + 2, 5).value = sum(map(int, salary))

wb.save('hometask_11_2.xlsx')
