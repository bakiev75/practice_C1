# создать класс Клиент, для хранения Имени, Фамилии, Города, Баланса.
# Вывод списка гостей. Добавить метод, который будет  возвращать информацию только об имени, фамилии и городе
# клиента

class Client:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance
    def __str__(self):
        return f'"{self.name} {self.surname}. {self.city}. Баланс: {self.balance} руб."'
    def get_guest(self):
        return f'{self.name} {self.surname}. г.{self.city}.'

client_1 = Client("Иван", "Петров", "Москва", 50)
client_2 = Client("Маргарита","Семенова","Уфа", 25)
client_3 = Client("Сергей","Смирнов","Владивосток", 150)

list_guests = [client_1,client_2, client_3]

for guest in list_guests:
    print(guest.get_guest())



