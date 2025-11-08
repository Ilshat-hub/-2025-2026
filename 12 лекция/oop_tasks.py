# Задание 1: Создание класса «Книга». Создайте класс Book, который будет представлять книгу.
# Он должен содержать следующие атрибуты: название, автор и год издания.
# Реализуйте метод для отображения информации о книге.

# Требования к демонстрации:
    # Создайте несколько объектов класса Book
    # Вызовите метод отображения информации для каждого объекта
    # Продемонстрируйте доступ к атрибутам объектов
    # Измените значение одного из атрибутов и покажите обновленную информацию
class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def display_info(self):
        print(f'Книга {self.name}, автор {self.author}, год {self.year}')

book = Book('name1', 'author1', 1234)
print(book.name)
print(book.author)
print(book.year)

book.display_info()
book.year = 1111

book.display_info()

# Задание 2: Класс «Автомобиль». Создайте класс Car, который будет представлять автомобиль.
# Он должен иметь атрибуты: марка, модель и год выпуска.
# Реализуйте метод для изменения года выпуска и метод для отображения информации об автомобиле.

# Требования к демонстрации:
    # Создайте несколько объектов класса Car
    # Вызовите метод отображения информации для каждого автомобиля
    # Используйте метод изменения года выпуска для одного из объектов
    # Покажите обновленную информацию после изменения
class Car:
    def __init__(self, marka, model, year):
        self.marka = marka
        self.model = model
        self.year = year
car1 = Car('Hyundai','Solaris', 2015 )
car2 = Car('KAMAZ','NeUbivaemaya', '♾️')
print(car1.marka, car1.model, car1.year)
print(car2.marka, car2.model, car2.year)

# Задание 3: Класс «Пользователь».
# Создайте класс User, который будет хранить информацию о пользователе: имя, электронную почту и пароль.
# Реализуйте метод для проверки корректности введенного пароля.
class User:
    def __init__(self, name, mail, password):
        self.name = name
        self.mail = mail
        self.password = password
    def proverka(self, pr_pass):
        if pr_pass == self.password:
            print('Пароль верный броо')
        else:
            print('ууу, пытаешься взломать?\n'
                  'ну я вызываю фсб небро')
            """while True:
                print('ПОПЫТКА ВЗЛОМА')"""
user1 = User('Владимир', 'KremlNePutin52@mail.com', 'Vovochka1952')
user2 = User('Дмитрий', 'KremlNeMedvedev65@mail.com', 'Dimon1965')
user1.proverka('123456789')
user1.proverka('Vovochka1952')
user2.proverka('123456789')
user2.proverka('Vovochka1952')
user2.password = '123456789'
user2.proverka('123456789')
# Требования к демонстрации:
    # Создайте несколько объектов класса User
    # Протестируйте метод проверки пароля с правильными и неправильными паролями
    # Продемонстрируйте доступ к атрибутам объектов
    # Измените пароль одного из пользователей и протестируйте проверку с новым паролем


# Задание 4: Класс «Прямоугольник». Создайте класс Rectangle, который будет представлять прямоугольник с заданной шириной и высотой.
# Реализуйте методы для вычисления площади и периметра прямоугольника.

# Требования к демонстрации:
    # Создайте несколько объектов класса Rectangle с разными размерами
    # Вызовите методы вычисления площади и периметра для каждого объекта
    # Измените размеры одного из прямоугольников
    # Покажите пересчитанные значения площади и периметра после изменения размеров
class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def area(self):
        return self.x * self.y
    def perimeter(self):
        return 2 * self.x + 2 * self.y
pr1 = Rectangle(1, 2)
pr2 = Rectangle(3, 4)
print(pr1.area())
print(pr1.perimeter())
print(pr2.area())
print(pr2.perimeter())
pr1.x = 5
pr1.y = 6
print(pr1.area())
print(pr1.perimeter())


