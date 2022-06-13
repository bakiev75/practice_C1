# Создать класс прямоугольника. Используя магический метод __str__ вернуть атрибуты
# прямоугольника в строку
# Создать метод, расчета площади фигуры. Вывести значение площади на экран.

class Rectangle:
    def __init__(self, x = 0, y = 0, width=0, heigth=0):
        self.x = x
        self.y = y
        self.width = width
        self.heigth = heigth
    def __str__(self):
        return f'Rectangle: {self.x}, {self.y}, {self.width}, {self.heigth}'
    def get_area(self):
        return f'Area = {self.width * self.heigth}'

rect_1 = Rectangle(5,10,50,100)
print(rect_1.__str__())
print(rect_1.get_area())

