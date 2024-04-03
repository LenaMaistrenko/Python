# Завдання 1
# Створіть клас Device, який містить інформацію про пристрій.
# За допомогою механізму успадкування реалізуйте клас
# CoffeeMachine (містить інформацію про кавомашину), клас
# Blender (містить інформацію про блендер), клас MeatGrinder
# (містить інформацію про м’ясорубку).
# Кожен із класів має містити необхідні для роботи методи

class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"Brand: {self.brand}, Model: {self.model}"


class CoffeeMachine(Device):
    def __init__(self, brand, model, type):
        super().__init__(brand, model)
        self.type = type

    def __str__(self):
        return super().__str__()+(f" Type: {self.type}")


class Blander:

    def __init__(self, brand, model, power):
        super().__init__(brand, model)
        self.power = power

    def __str__(self):
        return super().__str__() + (f" POwer: {self.power}")
class MeatGrinder:

    def __init__(self, brand, model, size):
        super().__init__(brand, model)
        self.size = size

    def __str__(self):
        return super().__str__() + (f" Size: {self.size}")



Завдання 2
Створіть клас Ship, який містить інформацію про кораблі.
За допомогою механізму успадкування реалізуйте клас
Frigate (містить інформацію про фрегат), клас Destroyer (містить
інформацію про есмінця), клас Cruiser (містить інформацію
про крейсер).
Кожен із класів має містити необхідні для роботи методи.


class Ship:
    def __init__(self, name, ship_type):
        self.name = name
        self.ship_type = ship_type

    def __str__(self):
        return f"Name: {self.name}, Type: {self.ship_type}"


class Frigate(Ship):
    def __init__(self, name, count):
        super().__init__(name, "Frigate")
        self.count = count

    def __str__(self):
        return super().__str__() + f", Missile count: {self.count}"



class Destroyer(Ship):
    def __init__(self, name, gun_size):
        super().__init__(name, "Destroyer")
        self.gun_size = gun_size

    def __str__(self):
        return super().__str__() + f", Gun size: {self.gun_size}mm"
class Cruiser(Ship):
    def __init__(self, name, aircraft_count):
        super().__init__(name, "Cruiser")
        self.aircraft_count = aircraft_count

    def __str__(self):
        return super().__str__() + f", Aircraft count: {self.aircraft_count}"