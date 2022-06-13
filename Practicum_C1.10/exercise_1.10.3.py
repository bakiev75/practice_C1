# создать класс Клиент, для хранения Имени, Фамилии, Города, Баланса.
# Вывод информации в строку, через точку "Иван Иванов. Москва. Баланс: 50 руб."

class Client:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance
    def __str__(self):
        return f'"{self.name} {self.surname}. {self.city}. Баланс: {self.balance} руб."'

client_1 = Client("Иван", "Петров", "Москва", 50)

print(client_1)

