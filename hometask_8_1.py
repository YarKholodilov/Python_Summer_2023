genomes = input('введите геном на русском языке: ').upper()
genom = genomes + '*'
edited = ''

for i in range(len(genom)-1):
    if genom[i] == 'А':
        edited += 'Г'
    elif genom[i] == 'Г':
        edited += 'А'
    elif (genom[i] == 'Ц' and genom[i + 1] == 'Т'):
        edited += genom[i] + 'АГ'
    elif (genom[i] == 'Т' and genom[i + 1] == 'Ц'):
        edited += genom[i] + 'АГ'
    else:
        edited += genom[i]
print(edited)



    # if A - G exchange
    # if C - T or T -C put AG
