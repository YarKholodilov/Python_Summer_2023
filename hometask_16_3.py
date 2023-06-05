def zaglavnaya(func):
    def wrapper():
        res = func()
        return res[0].title() + res[1:]
    return wrapper

@zaglavnaya
def to_text():
    return input('введите текст: ')

print(to_text())

# жили у бабуси два веселых гуся