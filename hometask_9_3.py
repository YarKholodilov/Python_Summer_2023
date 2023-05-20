from collections import Counter
s = input('введите предложение: ').replace(' ', '').lower()

# s = 'мАМа мыла Раму долго и упорно и никто не знает насколько долго'.replace(' ', '').lower()

a = Counter(s)
b = dict(a)

s = sorted(b.items(), key=lambda x: (-x[1], x[0]))[:10]
for i in range(len(s)):
        print(f'{s[i][0]} - {s[i][1]}')
