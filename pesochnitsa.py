class NonPositiveDigitException(ValueError):
    pass

class Square:
    def __init__(self, a):
        self.a = a
        if a <= 0:
            raise NonPositiveDigitException('Указана не положительная сторона квадрата')

    @property
    def area(self):
        return self.a ** 2

while True:
    try:
        b = Square(int(input("Введите сторону квадрата: ")))
        print("Площадь квадрата равна ", b.area)
    except NonPositiveDigitException:
        print("Ошибка - сторона квадрата не положительная")
    print()
    retry = input("Продолжим вычислять площадь квадрата? да / нет ")
    if retry == 'да':
        continue
    if retry == 'нет':
        break
    else:
        print("Вы не ввели да или нет. Поэтому - продолжим")
print("Конец программы")




































