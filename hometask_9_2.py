word = input("введите слово: ").lower()   # слово для которого ищем похожие
n = int(input('введите количество слов для сравнения: '))    # количество слов в которых ищем похожие
print(f"введите {n} слов: ")
similar = [input() for i in range(n)]   # формируем список из N слов
similar_indx = [[] for similars in range(n)]   # список вхождений гласных в каждом из N слов
vowels = "ауоыиэяюёе"
vow_index = []       #  индексы гласных в искомом слове, по сути шаблон для сравнения основных слов
answer = []        # список слов для ответа
for i in range(len(word)):            # поиск индексов гласных в искомом слове для списка
    if word[i] in vowels:
        vow_index.append(i)

for l in range(len(similar)):         # поиск индексов гласных в каждом из проверяемых слов и добавление в список
    for b in range(len((similar[l]))):
        if similar[l][b] in vowels:
             similar_indx[l].append(b)

for k in range(len(similar_indx)):         # проверка каждого слова на соответстие шаблону
    if similar_indx[k] == vow_index:
        answer.append(similar[k])

print(f'Cо словом "{word.upper()}" похожи следующие слова:')
if len(answer) == 0:
    print('Таких слов нет!')
else:
    print(*answer)