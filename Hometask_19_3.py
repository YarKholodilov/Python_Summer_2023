
class Person:
    def __init__(self, surname, name, middle_name):
        self.surname = surname.title()
        self.name = str(name).title()
        self.middle_name = str(middle_name).title()
    def __str__(self):
        return f'{self.surname}{self.name}{self.middle_name}'[::-1]


p = Person("Иванов", 'михаил', "Федорович")
print(p)