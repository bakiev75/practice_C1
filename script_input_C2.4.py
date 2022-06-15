
str_ = input("Введите число ")

try:
    a = int(str_)
except ValueError:
    print("Вы ввели неправильное число")
else:
    print(f"Вы ввели правильное число {a}")
finally:
    print("Выход из программы")
