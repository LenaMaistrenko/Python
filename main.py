#Homework
# маємо 4 списки цілих чисел. Обєднати в пятий спсок тількт ті елементи які є унікальними для кожного списку.
# Отриманий результат відсортуйте за спаданням чи зростанням за вибором користовача.
# Знайдіть значення, введене користувачем за дпомогою бінарного пошуку

import random
list1 = [random.randint(-10, 10) for i in range(10)]
list2 = [random.randint(-10, 10) for i in range(10)]
list3 = [random.randint(-10, 10) for i in range(10)]
list4 = [random.randint(-10, 10) for i in range(10)]
uniq1=[]
uniq2=[]
uniq3=[]
uniq4=[]

for i in range(len(list1)):
    if uniq1.count(list1[i]) == 0:
        uniq1.append(list1[i])
    if uniq2.count(list2[i]) == 0:
        uniq2.append(list2[i])
    if uniq3.count(list3[i]) == 0:
        uniq3.append(list3[i])
    if uniq4.count(list4[i]) == 0:
        uniq4.append(list4[i])
uniq = uniq1+uniq2+uniq3+uniq4
print("list1: ",list1,"uniq1: ", uniq1)
print("list2: ",list2,"uniq2: ", uniq2)
print("list3: ",list3,"uniq3: ", uniq3)
print("list4: ",list4,"uniq4: ", uniq4)
print("List of unique elements: ", uniq)

choice = int(input(" Sorting +  - 1, sorting -   2 : "))
if choice == 1:
    sortlist = sorted(uniq)
    print(sortlist)
elif choice == 2:
    sortlist = (sorted(uniq, reverse=True))
    print(sortlist)

else:
    print("wrong choice")

number = int(input("Input number : "))
sortlist = sorted(uniq)
left = 0
right = len(sortlist)-1
print(right)
while left <= right:
     mid = (left + right) // 2
     if sortlist[mid] == number:
         if choice ==1 :
            print(f"Your number {number} is on {mid} position on list")
            break
         else :
             print(f"Your number {number} is on {len(sortlist)-mid } position on list")
             break
     elif sortlist[mid] < number:
         left = mid + 1
     else:
         right = mid - 1

else:
     print(f"number {number} not found")



# Напишіть програму «Книги». Створіть два списки з даними. Один список зберігає назви книг, другий Реалізуйте меню для користувача:
# ■ відсортувати за назвою книг;
# відсортувати за рокам випуску;
# вивести список книг з назвами та роками випуску;
books = [("Книга1", 2005), ("Книга2", 2010), ("Книга3", 1998)]

while True:
    print("\nМеню:")
    print("1. Відсортувати за назвою книг")
    print("2. Відсортувати за роками випуску")
    print("3. Вивести список книг з назвами та роками випуску")
    print("4. Вихід")

    choice = input("Виберіть опцію: ")

    if choice == '1':
        sorted_books = sorted(books, key=lambda x: x[0])
        print("Відсортовано за назвою книг:")
        for book in sorted_books:
            print(f"Назва: {book[0]}, Рік випуску: {book[1]}")
    elif choice == '2':
        sorted_books = sorted(books, key=lambda x: x[1])
        print("Відсортовано за роками випуску:")
        for book in sorted_books:
            print(f"Назва: {book[0]}, Рік випуску: {book[1]}")
    elif choice == '3':
        print("Список книг:")
        for book in books:
            print(f"Назва: {book[0]}, Рік випуску: {book[1]}")
    elif choice == '4':
        break
    else:
        print("Некоректний вибір.")






# є список книг в форматі (автор, назва, рік, видання).створити меню. 1 Сортування книг за автором, або за роком . 2 ПОщук книги по назві, за виданням, автором.
# 3.фільтарація за роком. користвач водить рік та вибирає "показати киги після цього року" або "книги до цього року"

books = [
    ("Автор1", "Назва1", 2005, "Видання1"),
    ("Автор2", "Назва2", 2010, "Видання2"),
    ("Автор3", "Назва3", 1998, "Видання3")
]

while True:
    print("\nМеню:")
    print("1. Сортування книг за автором або за роком")
    print("2. Пошук книги за назвою, виданням або автором")
    print("3. Фільтрація за роком")
    print("4. Вихід")

    choice = input("Виберіть опцію: ")

    if choice == '1':
        sort_choice = input("Виберіть сортування: 1. За автором 2. За роком: ")
        if sort_choice == '1':
            sorted_books = sorted(books, key=lambda x: x[0])
            print("Відсортовано за автором:")
            for book in sorted_books:
                print(f"Автор: {book[0]}, Назва: {book[1]}, Рік: {book[2]}, Видання: {book[3]}")
        elif sort_choice == '2':
            sorted_books = sorted(books, key=lambda x: x[2])
            print("Відсортовано за роком:")
            for book in sorted_books:
                print(f"Автор: {book[0]}, Назва: {book[1]}, Рік: {book[2]}, Видання: {book[3]}")
        else:
            print("ПОмилка")
    elif choice == '2':
        search_term = input("Введіть назву, видання або автора книги для пошуку: ").lower()
        found_books = [book for book in books if search_term in [str(item).lower() for item in book]]
        if found_books:
            for book in found_books:
                print(f"Автор: {book[0]}, Назва: {book[1]}, Рік: {book[2]}, Видання: {book[3]}")
        else:
            print("Книга не знайдена.")
    elif choice == '3':
        filter_choice = input("1. Показати книги після вказаного року 2. Показати книги до вказаного року: ")
        year = int(input("Введіть рік: "))
        if filter_choice == '1':
            filtered_books = [book for book in books if book[2] > year]
        elif filter_choice == '2':
            filtered_books = [book for book in books if book[2] < year]
        else:
            print("Помилка")
            continue
        if filtered_books:
            print(f"Книги {'після' if filter_choice == '1' else 'до'} {year} року:")
            for book in filtered_books:
                print(f"Автор: {book[0]}, Назва: {book[1]}, Рік: {book[2]}, Видання: {book[3]}")
        else:
            print("Немає таких  книг ")
    elif choice == '4':
        break
    else:
        print("Некоректний вибір")


# Модуль 6. Кортежі, множини, словники
# Тема: Кортежі, множини, словники. Частина 1
# Початкова база книжкової колекції
# books = [
#     {'author': 'Джордж Оруелл', 'title': '1984', 'genre': 'Антиутопія', 'year': '1949', 'pages': '328', 'publisher': 'Secker & Warburg'},
#     {'author': 'Рей Бредбері', 'title': '451 градус за Фаренгейтом', 'genre': 'Антиутопія', 'year': '1953', 'pages': '158', 'publisher': 'Ballantine Books'},
#     {'author': 'Джордж Р. Р. Мартін', 'title': 'Гра Престолів', 'genre': 'Фентезі', 'year': '1996', 'pages': '694', 'publisher': 'Bantam Spectra'},
#     {'author': 'Сьюзен Коллінз', 'title': 'Голодні ігри', 'genre': 'Фантастика', 'year': '2008', 'pages': '374', 'publisher': 'Scholastic Press'},
#     {'author': 'Жуль Верн', 'title': 'Таємничий острів', 'genre': 'Пригодницький роман', 'year': '1874', 'pages': '532', 'publisher': 'Pierre-Jules Hetzel'}
# ]
#
# while True:
#     print("\nМеню:")
#     print("1. Додати книгу")
#     print("2. Видалити книгу")
#     print("3. Знайти книгу")
#     print("4. Змінити інформацію про книгу")
#     print("5. Показати всі книги")
#     print("6. Вихід")
#
#     choice = input("Оберіть опцію: ")
#
#     if choice == "1":
#         author = input("Введіть автора книги: ")
#         title = input("Введіть назву книги: ")
#         genre = input("Введіть жанр книги: ")
#         year = input("Введіть рік випуску книги: ")
#         pages = input("Введіть кількість сторінок книги: ")
#         publisher = input("Введіть видавництво книги: ")
#         book = {
#             'author': author,
#             'title': title,
#             'genre': genre,
#             'year': year,
#             'pages': pages,
#             'publisher': publisher
#         }
#         books.append(book)
#     elif choice == "2":
#         title = input("Введіть назву книги, яку потрібно видалити: ")
#         removed = False
#         for book in books:
#             if book['title'] == title:
#                 books.remove(book)
#                 print(f"Книга '{title}' видалена з колекції.")
#                 removed = True
#                 break
#         if not removed:
#             print(f"Книга з назвою '{title}' не знайдена в колекції.")
#     elif choice == "3":
#         title = input("Введіть назву книги, яку потрібно знайти: ")
#         found = False
#         for book in books:
#             if book['title'] == title:
#                 print("Інформація про книгу:")
#                 print("Автор:", book['author'])
#                 print("Назва:", book['title'])
#                 print("Жанр:", book['genre'])
#                 print("Рік випуску:", book['year'])
#                 print("Кількість сторінок:", book['pages'])
#                 print("Видавництво:", book['publisher'])
#                 found = True
#                 break
#         if not found:
#             print(f"Книга з назвою '{title}' не знайдена в колекції.")
#     elif choice == "4":
#         title = input("Введіть назву книги, для якої потрібно оновити інформацію: ")
#         field = input("Введіть поле, яке потрібно оновити: ")
#         new_value = input(f"Введіть нове значення для поля '{field}': ")
#         updated = False
#         for book in books:
#             if book['title'] == title:
#                 if field in book:
#                     book[field] = new_value
#                     print(f"Інформація про книгу '{title}' оновлена: {field} = {new_value}.")
#                     updated = True
#                     break
#                 else:
#                     print(f"Поле '{field}' не існує у записі про книгу.")
#                     updated = True
#                     break
#         if not updated:
#             print(f"Книга з назвою '{title}' не знайдена в колекції.")
#     elif choice == "5":
#         if not books:
#             print("У колекції немає книг.")
#         else:
#             print("Книжкова колекція:")
#             for i, book in enumerate(books, 1):
#                 print(f"{i}. {book['title']}")
#     elif choice == "6":
#         print("Програма завершена.")
#         break
#     else:
#         print("Некоректний вибір опції. Спробуйте ще раз.")

# Завдання 1
# Маємо три кортежі цілих чисел. Знайдіть елементи, які
# є у всіх кортежах.

# tuple1 = (1, 2, 7, 4, 5, 4, 2)
# tuple2 = (3, 4, 5, 6, 7, 4, 3)
# tuple3 = (5, 6, 7, 8, 9, 3, 1)
#
# result = set(tuple1)&set(tuple2)&set(tuple3)
# print("Спільні елементи ", result)

# Завдання 2
# Маємо три кортежі цілих чисел. Знайдіть елементи, які
# унікальні для кожного списку.

# tuple1 = (1, 2, 7, 4, 5, 4, 2)
# tuple2 = (3, 4, 1, 6, 7, 8, 13)
# tuple3 = (5, 6, 7, 8, 9, 3, 1)
#
# result1 = set(tuple1) - set(tuple2) - set(tuple3)
# result2 = set(tuple2) - set(tuple1) - set(tuple3)
# result3 = set(tuple3) - set(tuple1) - set(tuple2)
#
# print(" Унікальні значення tuple1: ", result1)
# print(" Унікальні значення tuple2: ", result2)
# print(" Унікальні значення tuple3: ", result3)

#
# Завдання 3
# Маємо три кортежі цілих чисел. Знайдіть елементи, які
# є в кожному з кортежів і знаходяться в кожному з них на тій
# самій позиції.

# tuple1 = (1, 2, 7, 4, 5, 4, 2)
# tuple2 = (3, 4, 7, 6, 7, 8, 13)
# tuple3 = (5, 6, 7, 8, 9, 3, 1)
#
# elements = []
#
# for i in range(min(len(tuple1),len(tuple2),len(tuple3))):
#     if tuple1[i] == tuple2[i] == tuple3[i]:
#         elements.append(tuple1[i])
#
# print(elements)
# Модуль 5. Сортування та пошук
# Тема: Сортування та пошук. Частина 1
# Завдання 1
# Відсортуйте перші дві третини списку в порядку зростання, якщо середнє арифметичне всіх елементів більше за нуль;
# якщо ні — тільки першу третину. Решту списку не сортуйте,
# а розташуйте у зворотному порядку.


# list = [3, -5, 1, -9, -2, 7, 6, -4, 8]
#
# average = sum(list) / len(list)
# print("average", average)
#
# if average >0:
#     index = (2 * len(list)) // 3
#     list1 = sorted(list[:index])
#     list2 = list[index:][::-1]
#     result = list1 + list2
#     print(result)
# else:
#     index = len(list) // 3
#     list1 = sorted(list[:index])
#     list2 = list[index:][::-1]
#     result = list1 + list2
#     print(result)

# Завдання 2
# Написати програму «Успішність». Користувач вводить
# 10 оцінок студента. Оцінки від 1 до 12. Реалізуйте меню для
# користувача:
# ■ виведення оцінок (виведення вмісту списку);
# ■ перескладання іспиту (користувач вводить номер елемента
# списку та нову оцінку);
# ■ отримання стипендії (стипендію отримують, якщо середній бал не нижче 10.7);
# ■ виведення відсортованого списку оцінок: за зростанням
# або спаданням.

# grades = []
# for i in range(10):
#     grade = int(input(f"Введіть оцінку від 1 до 12: "))
#     grades.append(grade)
#
# while True:
#     print("\nМеню:")
#     print("1. Виведення оцінок")
#     print("2. Перескладання іспиту")
#     print("3. Отримання стипендії")
#     print("4. Виведення відсортованого списку оцінок за зростанням")
#     print("5. Виведення відсортованого списку оцінок за спаданням")
#     print("6. Вихід")
#
#     choice = int(input("Виберіть пункт меню: "))
#
#     if choice == 1:
#         print(*grades)
#     elif choice ==2:
#         index = int(input("Введіть номер оцінки, яку потрібно змінити (від 1 до 10 ): "))
#         new_grade = int(input("Введіть нову оцінку (від 1 до 12): "))
#         grades[index-1] = new_grade
#         print("Оцінку замінено")
#     elif choice == 3:
#         average = sum(grades) / len(grades)
#         if average >= 10.7:
#             print("Студент отримує стипендію.")
#         else:
#             print("Студент не отримує стипендію.")
#     elif choice == 4:
#         print("Відсортований список оцінок за зростанням:", sorted(grades))
#     elif choice ==5:
#         print("Відсортований список оцінок за спаданням:", sorted(grades, reverse=True))
#     elif choice == 6:
#         print("Програма завершена.")
#         break

# Завдання 3
# Напишіть програму для сортування списку методом
# удосконаленого бульбашкового сортування. Удосконалення
# полягає в тому, щоб аналізувати кількість перестановок на
# кожному кроці. Якщо ця кількість дорівнює нулю, то продовжувати сортування немає сенсу — список відсортовано.

# import random
# list = [random.randint(0,10) for i in range(20)]
# print(list)
# n = len(list)
# for i in range(n):
#     fl = False
#     for j in range(0, n-i-1):
#         if list[j] > list[j+1]:
#             list[j], list[j+1] = list[j+1], list[j]
#             fl = True
#     if not fl:
#         break
#
# print("Відсортований список:", list)






# Модуль 3. Рядки, списки
# Тема: Списки. Частина 3
# Завдання
# Два списки цілих заповнюються випадковими числами.
# Сформуйте третій список, який містить:
# ■ елементи обох списків;
# ■ елементи обох списків без повторень;
# ■ елементи, спільні для двох списків;
# ■ тільки унікальні елементи кожного зі списків;
# ■ тільки мінімальне та максимальне значення кожного зі
# списків.
# import random
# list1 = [random.randint(0,10) for i in range(20)]
# list2 = [random.randint(0,10) for i in range(10)]
# list_uniq = []
# list_repit = []
# unique_list1 = []
# unique_list2 = []
#
#
# # ■ елементи обох списків;
# list3 = list1 + list2
#
# # ■ елементи обох списків без повторень;
# for i in list3:
#     if list_uniq.count(i) == 0:
#         list_uniq.append(i)
#
#
# # ■ елементи, спільні для двох списків;
# for i in list1:
#     if i in list2 and i not in list_repit:
#         list_repit.append(i)
#
# # ■ тільки унікальні елементи кожного зі списків;
# for i in list1:
#     if list1.count(i) == 1 and i not in unique_list1:
#         unique_list1.append(i)
# for i in list2:
#     if list2.count(i) == 1 and i not in unique_list2:
#         unique_list2.append(i)
#
#
# # ■ тільки мінімальне та максимальне значення кожного зі
# # списків.
# maxmin = [min(list1), max(list1),min(list2),max(list2)]
#
# print('list1: ',*list1)
# print('list2: ',*list2)
# print("елементи обох списків: ", *list3)
# print("елементи обох списків без повторень: ", *list_uniq)
# print("елементи, спільні для двох списків: ", *list_repit)
# print("тільки унікальні елементи кожного зі списків, list1: ", *unique_list1, "list2: ", *unique_list2)
# print('тільки мінімальне та максимальне значення  ', maxmin)












# У списку цілих, заповненому випадковими числами,
# розрахуйте:
# ■ Суму від’ємних чисел.
# ■ Суму парних чисел.
# ■ Суму непарних чисел.
# ■ Добуток елементів з індексами, кратними 3.
# ■ Добуток елементів між мінімальним та максимальним
# елементом.
# ■ Суму елементів, що знаходяться між першим та останнім додатним елементом.

# import random
#
# list = [random.randint(-10,10) for i in range(100)]
#
# sumnegative = sum( i for i in list if i < 0)
# parni = sum(i for i in list if i % 2 == 0)
# neparni =sum(i for i in list if i % 2 !=0)
# neparni =sum(i for i in list if i % 2 !=0)
#
# mult=1
# for i in range(0, len(list),3):
#     mult *= list[i]
#
#
#
#
# print (sumnegative,parni,neparni,mult)



# Завдання 2
# Маємо список цілих, заповнений випадковими числами. Використовуючи дані цього масиву створіть список
# цілих, що містить лише:
# ■ парні числа з першого списку;
# ■ непарні числа з першого списку;
# ■ від’ємні числа з першого списку;
# ■ додатні числа з першого списку.



# import random
#
# list = [random.randint(-100,100) for i in range(50)]
#
# even_numbers = [num for num in list if num % 2 == 0]
# odd_numbers = [num for num in list if num % 2 != 0]
# negative_numbers = [num for num in list if num < 0]
# positive_numbers = [num for num in list if num > 0]
# print('list: ', *list)
# print('even: ',*even_numbers)
# print('odd: ',*odd_numbers)
# print('-:',*negative_numbers)
# print("+",*positive_numbers)
# Модуль 3. Рядки, списки
# Тема: Списки. Частина 2

# Завдання 1
# Користувач вводить з клавіатури арифметичний вираз.
# Наприклад, 23+12.
# Виведіть результат виразу на екран. У нашому прикладі 35.
# Арифметичний вираз може складатися тільки з трьох частин:
# число, операція, число. Можливі операції: +, -, *, /.

# import re
# text = input("Enter math expression (example: 23+12): ")
#
# list = re.findall(r'\d+|\S', text)
# num1 = int(list[0])
# operator = list[1]
# num2 = int(list[2])
# if operator == '+':
#     result = num1 + num2
# elif operator == '-':
#     result = num1 - num2
# elif operator == '*':
#     result = num1 * num2
# elif operator == '/':
#     result = num1 / num2
# else:
#     print("Invalid operator")
#
# print(f"The result of the expression {text} is: {result}")
#
# Завдання 2
# У списку цілих, заповненому випадковими числами, визначте мінімальний та максимальний елементи, підрахуйте
# кількість від’ємних елементів, додатних елементів та кількість
# нулів. Результати виведіть на екран.

# import random
#
# numbers = [random.randint(-100, 100) for i in range(200)]
# print(numbers)
#
# max= max(numbers)
# min = min(numbers)
# null = numbers.count(0)
#
# negative_count = 0
# positive_count = 0
#
# for number in numbers:
#     if numbers[number] > 0:
#         positive_count += 1
#     elif numbers[number] < 0:
#         negative_count += 1




# print(f"max = {max}, min = {min}, null = {null} negative count = {negative_count}, positive count = {positive_count}")

# Homework строки

# Завдання 1
#Користувач вводить з клавіатури рядок. Перевірте, чи є
# введений рядок паліндромом. Паліндроми — слова, речення
# або текст, які однаково читаються як зліва направо, так і
# справа наліво

# str = input("Input string:")
# update_str = str.lower().replace(" ", "")
# revers_str = update_str[::-1]
# print("Its palindrome" if update_str == revers_str else "Its not palindrome")


# Завдання 2
# Користувач вводить з клавіатури деякий текст, а потім —
# список зарезервованих слів. Знайдіть в тексті всі зарезервовані слова та змініть їх регістр на верхній. Виведіть на екран
# змінений текст
# import re
# text = input('input text: ').split()
# words = input('input words (example: apple ball cat dog: ').split()
#
# for i in range(len(text)):
#      if text[i].lower() in words:
#         text[i] = text[i].upper()
#
# text = ' '.join(text)
#
# print("Modified text:", text)

# Завдання 3
# Маємо певний текст. Підрахуйте кількість пропозицій у
# цьому тексті та виведіть на екран отриманий результат.
# import re
#
# text ="""Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
# Expedita similique placeat ullam commodi iure voluptatum quidem tempore necessitatibus fuga at, inventore quaerat quos accusamus esse quis ullam, consequatur eaque vel eum earum iste officia, in exercitationem porro accusamus dolore, deserunt animi debitis voluptates. Eius aperiam laborum porro deserunt vitae et velit, assumenda at pariatur nulla magnam voluptates deserunt, repudiandae sed porro deleniti facilis quos excepturi magnam alias? Molestiae sunt blanditiis aperiam quam eaque quas, id perferendis animi nostrum eveniet veritatis non, dignissimos animi necessitatibus, odio porro praesentium sit incidunt in, reprehenderit atque fuga aliquam et debitis laudantium minus enim?
# Cum dignissimos ad eaque quae delectus accusamus doloribus inventore, ex sunt magni dolorum beatae rerum, rerum expedita voluptas odit aut consequatur eaque, quisquam commodi voluptas ab eum saepe tempore aperiam inventore labore quae, a ratione quibusdam perspiciatis hic laborum facilis? Suscipit commodi ipsa labore unde, quis dolores libero odit aliquam non animi molestias aliquid a magnam maxime, corporis id maiores in rem porro at aspernatur dicta quam mollitia quisquam?
# Quae ea id, dolorum maxime porro reprehenderit unde autem aspernatur incidunt soluta, ratione veniam non natus. Voluptate suscipit blanditiis odio facilis quia quos ut nemo dignissimos ducimus commodi, illum obcaecati minus, optio exercitationem temporibus rem assumenda perferendis reiciendis nulla illo placeat ea, est excepturi consequatur temporibus ex magnam aspernatur, non delectus laudantium. Assumenda est repellat nemo quia iste qui blanditiis, amet officia nihil minus repellat, ipsum praesentium quos autem magnam inventore ut, impedit dolorem necessitatibus quaerat quidem quo iure neque velit debitis minima, numquam eius consectetur in pariatur eveniet perferendis dignissimos saepe voluptatum ex.
# Temporibus hic ipsa, molestiae similique eveniet veritatis nisi sunt expedita natus porro maiores explicabo voluptas, magni consequuntur adipisci unde numquam labore doloremque placeat obcaecati tenetur? Nulla exercitationem ipsam praesentium velit obcaecati dolores magnam, cupiditate alias at expedita nobis temporibus laborum eos blanditiis, rem tempora cum voluptate consequuntur iste quas libero at tenetur repellat, eaque labore provident iusto sequi sunt, maiores dolor tenetur iste facilis fugit quis sint. Officia maxime architecto aspernatur iusto, quas sunt distinctio sapiente vitae nam voluptatibus doloremque minima aliquid in.
# Distinctio cupiditate fugiat praesentium in nam, accusantium laboriosam quae, nostrum quam rem amet nesciunt sint ad voluptas delectus exercitationem reprehenderit, quod tempora sit ut veritatis harum iusto mollitia eos ipsum quidem. Ratione assumenda numquam, magni soluta fugit totam porro cupiditate iusto doloribus sunt, nostrum quas architecto tempore assumenda alias veritatis obcaecati sapiente quae atque quia, ullam reprehenderit nostrum? """
#
# print(text)
# sentences = re.split(r'[.!?]', text)
#
# print(f"Number of sentences: {len(sentences)}")
#TEST


# Завдання 1
# Користувач вводить число. Визначте кількість цифр у
# цьому числі, підрахуйте їх суму та середнє арифметичне.
# Визначте кількість нулів у цьому числі. Спілкування з
# користувачем реалізуйте через меню.

# number = int(input("Enter a number: "))
#
# print("1  -  кількість цифр")
# print("2  -  сума цифр")
# print("3  -  середнє арифметичне")
# print("4  -  кількість нулів")
#
# choice = input("Enter your choice (1-4): ")
#
# num_str = str(number)
# sum = 0
# count = 0
# zero = 0
# while number > 0:
#     sum += number % 10
#     count += 1
#     if number % 10 == 0:
#         zero += 1
#     number //= 10
# average = sum / count
# if choice == '1':
#     print(f"кількість цифр: {len(num_str)}")
# elif choice == '2':
#     print(f"Сума цифр числа: {sum}")
# elif choice == '3':
#     print(f" Середнє арифметичне {average}")
# elif choice == '4':
#     print(f"Кількість нулів {zero}")

# Завдання 2
# Напишіть програму, яка виводить на екран шахівницю
# із заданим розміром клітинки. Наприклад, три:
# ***---***---***---***---
# ***---***---***---***---
# ***---***---***---***---
# ---***---***---***---***
# ---***---***---***---***
# ---***---***---***---***
# ***---***---***---***---
# ***---***---***---***---
# ***---***---***---***---
# ---***---***---***---***
# ---***---***---***---***
# ---***---***---***---***


# cell_size = int(input("Введіть розмір клітинки: "))
#
# for i in range(8):
#     for j in range(8):
#         if (i + j) % 2 == 0:
#             print("*" * cell_size, end="")
#         else:
#             print("-" * cell_size, end="")
#     print()




# Завдання 3
# Напишіть програму, яка перевіряє користувача на
# знання таблиці множення. Програма виводить на екран
# два числа, користувач повинен ввести їх добуток. Розробіть кілька
# рівнів складності (відрізняються складністю
# та кількістю питань). Виведіть користувачеві оцінку
#
# import random
#
# print("Start the quizz")
# level = int(input("Choose a level (1 - easy, 2 - medium, or 3  - hard): "))
# correct = 0
# incorrect = 0
# for i in range(5):
#     if level == 1:
#         num1 = random.randint(1, 9)
#         num2 = random.randint(1, 9)
#     elif level == 2:
#         num1 = random.randint(1, 9)
#         num2 = random.randint(10, 99)
#     else:
#         num1 = random.randint(10, 99)
#         num2 = random.randint(10, 99)
#
#     correct_answer = num1 * num2
#     user_answer = int(input(f"What is {num1} * {num2}? "))
#     if user_answer == correct_answer:
#         correct += 1
#     else:
#         incorrect += 1
# print("\nResults:")
# print(f"Correct Answers: {correct}")
# print(f"Incorrect Answers: {incorrect}")

# Завдання 4
# Виведіть на екран ромб із зірочок.


# height = int(input("Введіть висоту ромбу: "))
# for i in range(1, height + 1):
#     print(" " * (height - i) + "*" * (2 * i - 1))
#
# for i in range(height - 1, 0, -1):
#     print(" " * (height - i) + "*" * (2 * i - 1))

# Завдання 5
# Створіть гру «Вгадай число». Програма визначає число в діапазоні від 1 до 500.
# Користувач намагається його
# вгадати. Після кожної спроби, програма видає підказки –
# більше чи менше число за його загадане. Наприкінці програма видає
# статистику: за скільки спроб вгадано число
# і скільки часу це зайняло. Передбачте вихід якщо введе 0 у разі,
# якщо користувачеві набридло вгадувати число.

# import random
# import time
#
# number = random.randint(1, 500)
# print(number)
# start_time = time.time()
# count = 0
#
# while True:
#     answer = int(input("Input your number (1..500):  "))
#     count += 1
#
#     if answer == 0:
#         print(f"Exit. Number was {number}.")
#         break
#     elif answer == number:
#         end_time = time.time()
#         print(f"You win! Number was {number}. Count: {count}.Time: {(end_time-start_time):.2f} s.")
#     elif answer > number:
#         print('Your answer > ')
#     else:
#         print('Your answer <')


#Homework 5

# Завдання


# Таблиця множення
# num = int(input("Enter a number from 1 to 9: "))
# for i in range(1, 10):
#     result = i * num
#     print(f"{num} * {i} = {result}")
# print("End")



# Завдання 2
# Конвертор валют
# usd_to_uah = 39.2
# eur_to_uah = 43.3
# eur_to_usd = 1.10
# print("1. UAH\n2. USD\n3. EUR ")
# print("Exchange rate:\n\t1 USD = 39.2 UAH\n\t1 EUR = 43.3 UAH\n\t1 EUR = 1,10 USD")
# currency_original = int(input("Exchange from (enter 1,2 or 3): "))
# if currency_original == 1:
#     currency_original_name = "UAH"
# elif currency_original == 2:
#     currency_original_name = "USD"
# elif currency_original == 3:
#     currency_original_name = "EUR"
# else:
#     print("Invalid currency code.")
#     exit()
#
# currency_exchange = int(input("Exchange to (enter 1,2 or 3): "))
# if currency_exchange == 1:
#     currency_exchange_name = "UAH"
# elif currency_exchange == 2:
#     currency_exchange_name = "USD"
# elif currency_exchange == 3:
#     currency_exchange_name = "EUR"
# else:
#     print("Invalid currency code.")
#     exit()
#
# amount = float(input("Enter the amount: "))
# if currency_original == 1:
#     if currency_exchange == 2:
#         result = amount/usd_to_uah
#     elif currency_exchange == 3:
#         result = amount/eur_to_uah
#     else:
#         result = amount
# elif currency_original == 2:
#     if currency_exchange == 1:
#         result = amount*usd_to_uah
#     elif currency_exchange == 3:
#         result = amount/eur_to_usd
#     else:
#         result = amount
# elif currency_original == 3:
#     if currency_exchange == 1:
#         result = amount*eur_to_uah
#     elif currency_exchange == 2:
#         result = amount*eur_to_usd
#     else:
#         result = amount
# else:
#     result = amount
# print(f" Operation result: {amount} {currency_original_name} =  {result:.2f} {currency_exchange_name}")




#Завдання 3
# Перевірка на належність числа до вказаного діапазону чисел, вивід всього діапазону з позначенням вказаного числа за допомгою символу "!"

# bottom = int(input("Input the bottom: "))
# top = float(input("Input the top:"))
#
# while True:
#     number = int(input("Input number "))
#     if bottom <= number <= top:
#         for i in range(int(bottom), int(top) + 1):
#             if i == number:
#                 print(f"!{i}!", end=" ")
#             else:
#                 print(i, end=" ")
#         break
#     else:
#         print(f"{number} is not in the range. Please try again.")
























#Homework 4

# Завдання 1
# Користувач вводить з клавіатури число від 1 до 100. Якщо
# число кратне 3 (ділиться на 3 без остачі), виведіть слово «Fizz».
# Якщо число кратне 5, виведіть слово «Buzz». Якщо число
# кратне 3 та 5, потрібно вивести «Fizz Buzz». Якщо число не
# кратне ні 3, ані 5, виведіть тільки число.
# Якщо користувач ввів значення не в діапазоні від 1 до
# 100, виведіть повідомлення про помилку.

# print("="*20, "TASK 1", "="*20)
# num = int(input("Enter a number from 1 to 100: "))
# if 1 <= num <= 100:
#     if num % 3 == 0 and num % 5 == 0:
#         print("Fizz Buzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)
# else:
#     print("Wrong number ")
# print("end")

# Завдання 2
# Напишіть програму, яка на вибір користувача піднесе
# введене ним число до степеня від нульового до сьомого
# включно.

# num = int(input("Enter a number: "))
# exp = 0
#
# while exp <=7:
#     result = num ** exp
#     print(f"{num} ^ {exp} =  {result}")
#     exp +=1
# print("end")

#Завдання 3
# Напишіть програму підрахунку вартості розмови для
# різних мобільних операторів. Користувач вводить вартість
# розмови та вибирає, з якого на який оператор він дзвонить.
# Виведіть вартість розмови на екран.

# cost = float(input("Enter the cost of the call per minute: "))
# print("Choose mobile operators:")
# print("1. Kyivstar")
# print("2. Vodafone")
# print("3. lifecell")
#
# operator_from = int(input("Select your operator (1, 2, or 3): "))
# operator_to = int(input("Select the operator you are calling (1, 2, or 3): "))
#
# total = 0  # при условии,что звонки внутри сети бесплатные
# if operator_from == 1 and operator_to == 2 or operator_to == 3:
#     total = cost * 1.2
# elif operator_from == 2 and operator_to == 1 or operator_to == 3:
#     total = cost * 1.4
# elif operator_from == 3 and operator_to == 2 or operator_to == 1:
#     total = cost * 1.5
#
# print(f"Cost of the call: {total} ")

#Завдання 4
# Зарплата менеджера становить 200$ + відсоток від продажу:
# продаж до 500$ – 3%, 500 –1000$ – 5%, понад 1000$ – 8%. Користувач вводить з
# клавіатури рівень продажу для трьох менеджерів. Визначте їхню зарплату, а також найкращого менеджера,
# нарахуйте йому премію 200$ та виведіть підсумки на екран.

#
# manager1 = int(input("Enter the sales level for Manager 1: "))
# manager2 = int(input("Enter the sales level for Manager 2:"))
# manager3 = int(input("Enter the sales level for Manager 3:"))
#
# salary1 = 0
# salary2 = 0
# salary3 = 0
# bonus = 0
#
# if 0 < manager1 < 500:
#     bonus = 1.03
# elif 500 <= manager1 <= 1000:
#     bonus = 1.05
# elif manager1 > 1000:
#     bonus = 1.08
# salary1 = 200*bonus
# if 0 < manager2 < 500:
#     bonus = 1.03
# elif 500 <= manager2 <= 1000:
#     bonus = 1.05
# elif manager2 > 1000:
#     bonus = 1.08
# salary2 = 200 * bonus
# if 0 < manager3 < 500:
#     bonus = 1.03
# elif 500 <= manager3 <= 1000:
#     bonus = 1.05
# elif manager3 > 1000:
#     bonus = 1.08
# salary3 = 200 * bonus
#
# bestmanager = max(salary1, salary2, salary3)
# if bestmanager == salary1:
#     salary1 += 200
# elif bestmanager == salary2:
#     salary2 += 200
# elif bestmanager == salary3:
#     salary3 += 200
#
# print(f"Salary for Manager 1: ${salary1}")
# print(f"Salary for Manager 2: ${salary2}")
# print(f"Salary for Manager 3: ${salary3}")

#millioner

# budget = 0
# print("2+2=?")
# print("""
#     1)2     2)4
#     3)18    4)3
# """)

#chess
# x1 = int(input("Input x1 : "))
# y1 = int(input("Input  y1: "))
# x2 = int(input("Input x2 : "))
# y2 = int(input("Input  y2: "))
#
# if ((x1 and y1 and x2 and y2) >= 1) and ((x1 and y1 and x2 and y2) <= 8):
#     if x1 == x2:
#         print("can kill")
#     elif y1 == y2:
#         print("can kill")
#     else:
#         print("can't kill")
# else:
#     print("wrong numbers")

#chess2

# x1 = int(input("Input x1 : "))
# y1 = int(input("Input y1: "))
# x2 = int(input("Input x2 : "))
# y2 = int(input("Input y2: "))
# if 1 <= x1 <= 8 and 1 <= x1 <= 8 and  1 <= x1 <= 8 and 1 <= x1 <=8:
# # if ((x1 and y1 and x2 and y2) >= 1) and ((x1 and y1 and x2 and y2) <= 8):
#     if abs(x1-x2) == abs(y1-y2):
#         print("yes")
#     else:
#         print("no")
# else:
#     print("wrong numbers")

# chess3

# x1 = int(input("Input x1 : "))
# y1 = int(input("Input y1: "))
# x2 = int(input("Input x2 : "))
# y2 = int(input("Input y2: "))
# if 1 <= x1 <= 8 and 1 <= x2 <= 8 and 1 <= y1 <= 8 and 1 <= y2 <= 8:
#     if (abs(x1 - x2) == 1 and abs(y1 - y2) == 2) or (abs(x1 - x2) == 2 and abs(y1 - y2) == 1):
#         print("yes")
#     else:
#         print("no")
# else:
#     print("wrong numbers")









    #Homework3


#Task1
# Користувач вводить з клавіатури три числа. Залежно від
# вибору користувача, програма виводить на екран суму трьох
# чисел або добуток трьох чисел.

# print("="*20, "TASK 1", "="*20)
# a = int(input("Input a : "))
# b = int(input("Input b : "))
# c = int(input("Input c : "))
# symb = input("Enter action (+ or *) : ")
# result = "Result:  {:d} {:s} {:d} {:s} {:d} = {:d}"
# if symb == "+":
#     print(result.format(a, symb, b, symb, c, a+b+c))
# elif symb == "*":
#     print(result.format(a, symb, b, symb, c, a*b*c))
# else:
#     print("Unknown action")
# print("Finish")

#Task2
# Користувач вводить з клавіатури три числа. Залежно від
# вибору користувача, програма виводить на екран максимум із
# трьох, мінімум із трьох або середньоарифметичне трьох чисел.

# print("="*20, "TASK 2", "="*20)
# a = int(input("Input a : "))
# b = int(input("Input b : "))
# c = int(input("Input c : "))
# operation = (input("Input operation (min, max, average): "))
# if operation == "min":
#     result = min(a, b, c)
#     print(f"The minimum of {a}, {b} and {c} is: {result}")
# elif operation == "max":
#     result = max(a, b, c)
#     print(f"The maximum of {a}, {b} and {c} is: {result}")
# elif operation == "average":
#     result = (a+b+c)/3
#     print(f"The average of {a}, {b} and {c} is: {result}")
# else:
#     print("Unknown operation")
# print("Finish")


#Task3
# Користувач вводить з клавіатури якусь кількість метрів.
# Залежно від вибору користувача, програма конвертує метри
# в милі, дюйми або ярди.

# print("="*20, "TASK 3", "="*20)
# meter = int(input("Input amount of meters: "))
# exchange = (input (" What exchange do you need? (mile, inch, or yard): "))
# if exchange == "mile":
#     print(f"{meter} meters = {meter * 0.0006} miles")
# elif exchange == "inch":
#     print(f"{meter} meters = {meter * 39.37} inches")
# elif exchange == "yard":
#     print(f"{meter} meters = {meter * 1.09} yards")
# else:
#     print("Unknown operation")
# print("Finish")












#Homework2
# # Task1
# print("="*20 , "TASK 1", "="*20)
# a = float(input("Input a : "))
# b = float(input("Input b : "))
# c = float(input("Input c : "))
# print(" Your numbers are: a = ", a, "b = ", b, "c = ", c)
# print("a+b+c = ", a+b+c)
# print("a*b*c = ", a*b*c)
#
# # Task2
# print("="*20 , "TASK 2", "="*20)
# salary = float(input("Enter your monthly salary : "))
# credit = float(input("Enter your monthly credit payment : "))
# rent = float(input("Enter your monthly rent : "))
# balance = salary - credit - rent
# balance = round(balance, 2)
# print(f"Remaining balance after all payments: {balance}")
#
# # Task3
# print("="*20, "TASK 3", "="*20)
# diagonal1 = float(input("Enter the length of the first diagonal of the romb: "))
# diagonal2 = float(input("Enter the length of the second diagonal of the romb: "))
# area = 0.5 * diagonal1 * diagonal2
# print(f"The area of the romb with diagonals {diagonal1} and {diagonal2} is {area}")
#
# #Task4
# print("="*20 , "TASK 4", "="*20)
# print("To be\nor not\nto be")
#
# #Task5
# print("="*20 , "TASK 5", "="*20)
# print('"Life is what happens\n\twhen\n\t\tyou’re busy making other plans.\b"\n\t\t\t\t\t\t\tJohn Lennon')

