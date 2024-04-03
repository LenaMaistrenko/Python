# Курс: «Введення в мову
# програмування Python
# Модуль 9. Об’єктно-орієнтоване програмування
# Тема: Класи. Об’єкти. Частина 1
# Завдання 1
# Реалізуйте клас «Автомобіль». Збережіть у класі: назву
# моделі, рік випуску, виробника, об’єм двигуна, колір машини,
# ціну. Реалізуйте методи класу для введення-виведення даних
# та інших операцій.

class Car:
    def __init__(self, model, year, manufacturer, engine, color, price):
        self._model = model
        self._year = year
        self._manufacturer = manufacturer
        self._engine = engine
        self._color = color
        self._price = price

    def get_model(self):
        return self._model

    def get_year(self):
        return self._year

    def get_manufacturer(self):
        return self._manufacturer

    def get_engine(self):
        return self._engine

    def get_color(self):
        return self._color

    def get_price(self):
        return self._price

    def set_model(self, new_model):
        self._model = new_model

    def set_year(self, new_year):
        self._year = new_year

    def set_manufacturer(self, new_manufacturer):
        self._manufacturer = new_manufacturer

    def set_engine_capacity(self, new_engine):
        self._engine = new_engine

    def set_color(self, new_color):
        self._color = new_color

    def set_price(self, new_price):
        self._price = new_price

    def display_info(self):
        print("Model:", self._model)
        print("Year:", self._year)
        print("Manufacturer:", self._manufacturer)
        print("Engine:", self._engine)
        print("Color:", self._color)
        print("Price:", self._price)


car1 = Car("Toyota Camry", 2022, "Toyota", "2.5L", "red", 10000)
car1.display_info()

print("Price:", car1.get_price())

car1.set_price(11000)
print("New price:", car1.get_price())
# Завдання 2
# Реалізуйте клас «Книга». Збережіть у класі: назву книги,
# рік видання, видавця, жанр, автора, ціну. Реалізуйте методи
# класу для введення-виведення даних та інших операцій.

class Book:
    def __init__(self, title, year,publisher, genre, author, price ):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def display_info(self):
        print("Title:", self.title)
        print("Year:", self.year)
        print("Publisher:", self.publisher)
        print("Genre:", self.genre)
        print("Author:", self.author)
        print("Price:", self.price)

    def set_price(self, new_price):
        self.price = new_price
        print("New price:", self.price)


book1 = Book("Red Hat", 1950, "ABC", "story", "Grimm", 200)
book1.display_info()

book1.set_price(300)
book1.display_info()
# Завдання 3
# Реалізуйте клас «Стадіон». Збережіть у класі: назву стадіону, дату відкриття, країну, місто, місткість. Реалізуйте методи
# класу для введення-виведення даних та інших операцій


class Stadium:
    def __init__(self, name, opening_date, country, city, capacity):
        self._name = name
        self._opening_date = opening_date
        self._country = country
        self._city = city
        self._capacity = capacity

    def get_name(self):
        return self._name

    def get_opening_date(self):
        return self._opening_date

    def get_country(self):
        return self._country

    def get_city(self):
        return self._city

    def get_capacity(self):
        return self._capacity

    def set_capacity(self, new_capacity):
        self._capacity = new_capacity
        print("New cappacity:", self._capacity)

    def display_info(self):
        print("Name:", self._name)
        print("OPenning date:", self._opening_date)
        print("country:", self._country)
        print("City:", self._city)
        print("Capacity:", self._capacity)

stadium1 = Stadium("Metallist", "01 01 1950", "Ukraine", "Kharkiv", 50000)
stadium1.display_info()
stadium1.set_capacity(55000)
stadium1.display_info()