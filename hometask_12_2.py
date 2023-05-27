n = int(input())

print(''.join(list(k for k in [(str(i)+'*') * i for i in range(1, n+1)])).replace('*', ',').replace(' ', '')[:-1].replace(',', ', '))
