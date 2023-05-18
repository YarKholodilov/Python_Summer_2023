spisok = ['aafb', 'rqx', 'a', 'adava']

print(sorted(spisok, key=lambda spisok: (-len(set(spisok)), sorted(spisok))))
