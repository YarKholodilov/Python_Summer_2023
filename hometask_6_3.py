from string import punctuation
text = input()
buk, dug, punk = '', '', ''

for i in text:
    if i.isdigit():
        buk += i + ' '
    elif i.isalpha():
        dug += i + ' '
    elif i in punctuation:
        punk += i + ' '

print(buk)
print(dug)
print(punk)
