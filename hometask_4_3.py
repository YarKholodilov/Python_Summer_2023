text = input('введите 2 текста разделенных точкой: ').lower().split('.')
# привел все буквы к нижнему регистру для сравнения текста

sentance_1, sentance_2 = '', ''
dct_1, dct_2 = dict(), dict()

# в этих 2 циклах убираю все символы кроме букв
for symbol in text[0]:
    if symbol.isalpha():
        sentance_1 += symbol

for symbol in text[1]:
    if symbol.isalpha():
        sentance_2 += symbol

# в словарях ключи - буквы, а в значениях подсчитываю их количество
for key in sentance_1:
    if key not in dct_1:
        dct_1[key] = dct_1.get(key, 1)
    else:
        dct_1[key] = dct_1.get(key) + 1

for key in sentance_2:
    if key not in dct_2:
        dct_2[key] = dct_2.get(key, 1)
    else:
        dct_2[key] = dct_2.get(key) + 1
#print(dct_2, dct_1)

# сравниваю словари на одинаковые ключи и на одинаковые значения
if (sorted(dct_1.keys()) and sorted(dct_1.values())) == \
        (sorted(dct_2.keys()) and sorted(dct_2.values())):
    print('True')
else:
    print('False')