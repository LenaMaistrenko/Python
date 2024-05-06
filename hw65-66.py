# Завдання 1
#
# Користувач вводить з клавіатури набір чисел. Отримані
# числа необхідно зберегти до списку (тип списку оберіть в за-
# лежності від поставленого нижче завдання). Після чого пока-
# жіть меню, в якому запропонуєте користувачеві набір пунктів:
#
#   . Додати нове число до списку (якщо таке число існує у
# списку, потрібно вивести повідомлення про це користу-
# вачеві без додавання числа).
#
# . Видалити усі входження числа зі списку (користувач вво-
#
# дить з клавіатури число для видалення)
#
# . Показати вміст списку (залежно від вибору користувача,
#
# покажіть список з початку або з кінця)
#
# . Перевірити, чи є значення у списку
# . Замінити значення у списку (користувач визначає, чи
#
# замінити тільки перше входження, чи всі)
#
# Дія виконується залежно від вибору користувача

class Penalty:
    def __init__(self, penalty_type, city):
        self.penalty_type = penalty_type
        self.city = city

class Person:
    def __init__(self, personal_id, name, city):
        self.personal_id = personal_id
        self.name = name
        self.city = city
        self.penalties = []

    def add_penalty(self, penalty_type, city):
        self.penalties.append(Penalty(penalty_type, city))

class Node:
    def __init__(self, person):
        self.person = person
        self.left = None
        self.right = None

class Database:
    def __init__(self):
        self.root = None

    def add_person(self, personal_id, name, city):
        person = Person(personal_id, name, city)
        if self.root is None:
            self.root = Node(person)
        else:
            self._add_person(self.root, person)

    def _add_person(self, root, person):
        if person.personal_id < root.person.personal_id:
            if root.left is None:
                root.left = Node(person)
            else:
                self._add_person(root.left, person)
        elif person.personal_id > root.person.personal_id:
            if root.right is None:
                root.right = Node(person)
            else:
                self._add_person(root.right, person)
        else:
            print("Person with this personal ID already exists.")

    def add_penalty(self, personal_id, penalty_type, city):
        person = self.find_person(self.root, personal_id)
        if person:
            person.add_penalty(penalty_type, city)
            print("Penalty added for the person.")
        else:
            print("Person with this personal ID does not exist.")

    def remove_penalty(self, personal_id, penalty_type, city):
        person = self.find_person(self.root, personal_id)
        if person:
            penalties = person.penalties
            for penalty in penalties:
                if penalty.penalty_type == penalty_type and penalty.city == city:
                    penalties.remove(penalty)
                    print("Penalty removed successfully.")
                    return
            print("Penalty not found for this person.")
        else:
            print("Person with this personal ID does not exist.")

    def print_full_database(self):
        print("Database:")
        self._print_full_database(self.root)

    def _print_full_database(self, root):
        if root:
            self._print_full_database(root.left)
            print("Personal ID:", root.person.personal_id)
            print("Name:", root.person.name)
            print("City:", root.person.city)
            print("Penalties:")
            for penalty in root.person.penalties:
                print("- Type:", penalty.penalty_type, "| City:", penalty.city)
            self._print_full_database(root.right)

    def print_by_city(self, city):
        print("People in", city, "city:")
        self._print_by_city(self.root, city)

    def _print_by_city(self, root, city):
        if root:
            self._print_by_city(root.left, city)
            if root.person.city == city:
                print("- Personal ID:", root.person.personal_id, "| Name:", root.person.name)
            self._print_by_city(root.right, city)

    def find_person(self, root, personal_id):
        if root is None or root.person.personal_id == personal_id:
            return root.person if root else None
        if personal_id < root.person.personal_id:
            return self.find_person(root.left, personal_id)
        return self.find_person(root.right, personal_id)

def main():
    db = Database()

    while True:
        print("\nMenu:")
        print("1. Add a new person to the database")
        print("2. Add a penalty for an existing person")
        print("3. Remove a penalty for an existing person")
        print("4. Print full database")
        print("5. Print people by city")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            personal_id = int(input("Enter personal ID: "))
            name = input("Enter name: ")
            city = input("Enter city: ")
            db.add_person(personal_id, name, city)
        elif choice == "2":
            personal_id = int(input("Enter personal ID: "))
            penalty_type = input("Enter penalty type: ")
            city = input("Enter city: ")
            db.add_penalty(personal_id, penalty_type, city)
        elif choice == "3":
            personal_id = int(input("Enter personal ID: "))
            penalty_type = input("Enter penalty type: ")
            city = input("Enter city: ")
            db.remove_penalty(personal_id, penalty_type, city)
        elif choice == "4":
            db.print_full_database()
        elif choice == "5":
            city = input("Enter city: ")
            db.print_by_city(city)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
