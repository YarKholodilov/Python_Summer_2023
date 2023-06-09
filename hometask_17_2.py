def up_list(func):
    def wrapper(*args):
        lst = []
        for i in args:
            lst.append(i.upper())
        func(*args)
        return lst
    return wrapper


@up_list
def test(*args):
    pass

print(test("аргумент1", "аргумент2", 'AРГумент3'))


formula = 'formula'
thesis = 'thesis'
conclusion = 'conclusion'
@up_list
def matematik(*args):
    pass

print(matematik(formula, thesis, conclusion))



# ['АРГУМЕНТ1', 'АРГУМЕНТ2', 'AРГУМЕНТ3']
# ['FORMULA', 'THESIS', 'CONCLUSION']