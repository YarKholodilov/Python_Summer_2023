class Shape():
    def __init__(self, color, square):
        self.color = color
        self.square = square

    def set_color(self, color):
        self.color = color

    def get_color(self):
        print(f"Объект имеет {self.color} цвет")

    def set_square(self, square):
        self.square = square

    def get_square(self):
        print(f"Объект имеет площадь {self.square}")


triange = Shape('Красный', 100)
circle = Shape('Синий', 250)

triange.get_color()
triange.set_color('Зеленый')
triange.get_color()
print(triange.color, triange.square)
triange.set_square(300)
triange.get_square()


circle.get_color()
circle.set_color('Оранжевый')
circle.get_color()
print(circle.color, circle.square)
circle.set_square(200)
print(circle.color)
circle.get_square()







