dna = input().upper()
rna = ''
for i in dna:
    if i == 'A':
        rna += 'U'         # Uracil
    if i == 'T':
        rna += 'A'
    if i == 'G':
        rna += 'C'
    if i == 'C':
        rna += 'G'

print(rna)