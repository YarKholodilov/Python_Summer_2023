
peter = set(input('введите книги Пети через запятую: ').lstrip().lower().split(', '))
maria = set(input('введите книги Маши через запятую: ').lstrip().lower().split(', '))

print('Количество одиннаковых книг, прочитанных учениками:')
print(len(peter & maria))




# война и мир, ведьмак, гулливер, идиот, портрет дориана грея, пикник на обочине
# идиот, щелкунчик, алиса в стране чудес, преступление и наказание, гулливер, ведьмак