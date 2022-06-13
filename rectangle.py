
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_width(self):
        return self.width

    def get_heigth(self):
        return self.height

    # Метод, рассчитывающий площадь

    def get_area(self):
        return self.width * self.height

