genomes = input('введите геном на русском языке: ').upper()
edited = ''

if 'АГ' in genomes:
    genomes = genomes.replace('АГ', '&&') # ('АГ', 'ГА')
if 'ГА' in genomes:
    genomes = genomes.replace("ГА", "@@")

genomes = genomes.replace('@@', 'АГ')
genomes = genomes.replace('&&', 'ГА')
genom = genomes + '*'

for i in range(len(genom)-1):
    if (genom[i] == 'Ц' and genom[i + 1] == 'Т'):
        edited += genom[i] + 'АГ'
    elif (genom[i] == 'Т' and genom[i + 1] == 'Ц'):
        edited += genom[i] + 'АГ'
    else:
        edited += genom[i]
print(edited)
