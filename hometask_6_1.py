rome = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, '*': 0}
n_r = input('введите римсое число: ').upper()
r_num = n_r + '*'
dec_n = 0
for i in range(0, len(r_num)-1):
    if r_num[i] in rome.keys():
        if rome[r_num[i+1]] <= rome[r_num[i]]:
            dec_n += rome[r_num[i]]

        elif rome[r_num[i]] < rome[r_num[i+1]]:
            dec_n -= rome[r_num[i]]

print(dec_n)