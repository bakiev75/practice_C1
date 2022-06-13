class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f'Dot: {self.x,self.y}'

class Circle:
    def __init__(self, r):
        self.r = r

    def circle_area(self):
        return 3.14 * self.r ** 2

p1 = Dot(1,2)
p2 = Dot(1,3)

print(p1==p2)
print(p1)
print(p2)

c_1 = Circle(10)

print(c_1.circle_area())