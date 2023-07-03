# создание метакласса
def dis(self):
    for k, v in self.__dict__.items():
            print(f'{k} - {v}')


Pet = type('Pet', (), {'dis': dis})

my_pet = Pet()
my_pet.name = 'Tom'
my_pet.age = 14
print(my_pet.dis())
