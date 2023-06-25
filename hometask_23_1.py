text = 'aabbsaccdtdccas'
# text = input('введите текст: ')
forwards = []
forwards.append(text)

if text == text[::-1]:
    print(len(text))
else:
    for i in range(1, len(text)):
        forwards.append(text[i:len(text)])
        forwards.append(text[:-i])

for i in range(len(forwards)):
    if forwards[i] == forwards[i][::-1]:
        print(len(forwards[i]))
        break

