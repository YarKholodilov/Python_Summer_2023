text = input('введите текст: ')
new_text = text.split()
max_word = ''
clear_text = []
for word in new_text: # убираю знаки приписания и цифры из текста
    for letter in word:
        if letter.isalpha() != True:
            word = word.replace(letter, ' ').rstrip()
    clear_text.append(word)

if len(clear_text) == 1:
    print(clear_text[0])

else:
    for i in range(len(clear_text)): # ищем максимально длинное слово
        if len(clear_text[i]) > len(max_word):
            max_word = clear_text[i]
    # print(max_word)
    for i in clear_text:  # ищем одиннаковые с максимальным по длине слова
        if len(i) == len(max_word):
            print(i)