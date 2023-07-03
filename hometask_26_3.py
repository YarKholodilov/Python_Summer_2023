
class Person:
    def __init__(self, name):
        self.name = name
        self.__age = 0

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 0 <= age < 100:
            self.__age = age
        else:
            raise ValueError('Недопустимы возраст')

    @age.deleter
    def age(self):
         del self.__age



m = Person('Alexey')
# m.age = 101
# m.age = 85
m.age = 12
print(m.__dict__)

