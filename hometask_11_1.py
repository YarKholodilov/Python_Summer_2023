import calendar, locale

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
free_visit = []
year = 2023

for m in range(1, 13):
    months = calendar.Calendar().monthdayscalendar(year, m)
    if months[0][3] != 0:
        free_visit.append(f'{months[2][3]} {calendar.month_name[m].title()} ')
    else:
        free_visit.append(f'{months[3][3]} {calendar.month_name[m].title()} ')

print(f'В {year} году вы сможете бесплатно посетить "Эрмитаж" в следующие даты: ')
print(*free_visit, sep='\n')
