def MakeCamel(text):
    return text.title().replace(' ', '')

tx = input('введите текст через пробел: ')
print(MakeCamel(tx))