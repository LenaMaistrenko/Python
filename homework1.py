# Завдання 1
# Створіть функцію, яка повертає всі непарні числа в діапазоні.
# Функція приймає початок і кінець діапазону як параметри. Використовуйте механізм генераторів усередині функції.

def oddelem(start, end):
    for i in range(start, end):
        if i % 2 != 0:
            yield i

result = oddelem(2,10)
print(list(result))

# Завдання 2
# Створіть функцію, яка повертає всі значення зі списку, що не перебувають у діапазоні, зазначеному користувачем.
# Функція приймає список, початок і кінець діапазону як параметри. Використовуйте механізм генераторів усередині функції.

def values_not_in_range(lst, start_range, end_range):
    for num in lst:
        if num < start_range or num > end_range:
            yield num

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
start_range = 3
end_range = 7
result = values_not_in_range(my_list, start_range, end_range)
print("Values not in the range from", start_range, "to", end_range, ":", list(result))

# Завдання 3
# Для виконання цього завдання обовязково використовуйте механізм функцій вищого порядку (higher order functions).
# Створіть функцію, що відображає лінію (горизонтальну або вертикальну)'
# з використанням символу, зазначеного користувачем. Користувач визначає символ і яку лінію відображати.)

def hline(symbol):
    print(symbol * 5)

def vline(symbol):
    for i in range(1, 5):
        print(symbol)


def show(symbol, fun):
    fun(symbol)

symbol = input("Input symbol: ")
type = input("Input type (h or v)")

if type == 'h':
    show(symbol, hline)
elif type == 'v':
    show(symbol, vline)
else:
    print("Try again")

# Завдання 4
# Створіть функцію, що повертає список з усіма парними числами, від 0 до 100000.
# Використовуючи механізм декораторів, порахуйте скільки секунд знадобилося для обчислення всіх чисел.
# Відобразіть на екран кількість секунд і всі парні числа від 0 до 100 000.

import time

def calculate_time(func):
    def wrapper():
        start_time = time.time()
        result = func()
        end_time = time.time()
        print("Time taken: {:.6f} seconds".format(end_time - start_time))
        return result
    return wrapper

@calculate_time
def get_even_numbers():
    even_numbers = [num for num in range(0, 100001) if num % 2 == 0]
    return even_numbers

print("Even Numbers:")
even_numbers_list = get_even_numbers()
print(even_numbers_list)

# Завдання 5
# Додайте до четвертого завдання можливість передавати межі діапазону для пошуку всіх парних чисел.
import time

def calculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("Time taken: {:.6f} seconds".format(end_time - start_time))
        return result
    return wrapper

@calculate_time
def get_even_numbers(start, end):
    even_numbers = [num for num in range(start, end + 1) if num % 2 == 0]
    return even_numbers

start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

print("Even Numbers in the range from", start_range, "to", end_range)
even_numbers_list = get_even_numbers(start_range, end_range)
print(even_numbers_list)
