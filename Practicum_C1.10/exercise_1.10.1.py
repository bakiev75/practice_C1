# Создать класс прямоугольника. Используя магический метод __str__ вернуть атрибуты
# прямоугольника в строку

class Rectangle:
    def __init__(self, x = 0, y = 0, width=0, height=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def __str__(self):
        return f'Rectangle: {self.x}, {self.y}, {self.width}, {self.height}'

rect_1 = Rectangle(5,10,50,100)
print(rect_1.__str__)


