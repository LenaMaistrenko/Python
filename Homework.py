# Модуль 4. Функції
# Тема: Функції. Частина 2
# Завдання 1
# Напишіть функцію для підрахунку добутку елементів
# списку цілих. Список передається як параметр. Отриманий
# результат повертається із функції.

def calculate(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

numbers = [2, 3, 4, 5]
result = calculate(numbers)
print(result)

# Завдання 2
# Напишіть функцію для знаходження мінімуму в списку
# цілих. Список передається як параметр. Отриманий результат
# повертається із функції.

def minimum(numbers):
    minnumber = numbers[0]
    for num in numbers:
        if num < minnumber:
            minnumber = num
    return minnumber

numbers = [2, 3, 4, 5, 1]
result = minimum(numbers)
print(result)

# Завдання 3
# Напишіть функцію, яка визначає кількість простих чисел
# у списку цілих. Список передається як параметр. Отриманий
# результат повертається із функції.

def count_primes(lst):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    count = 0
    for num in lst:
        if is_prime(num):
            count += 1
    return count

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
result = count_primes(numbers)
print(result)

# Завдання 4
# Напишіть функцію, яка видаляє зі списку цілих певне
# задане число. З функції потрібно повернути кількість віддалених елементів.



def delnum(numbers, number):
    count = numbers.count(number)
    numbers = [num for num in numbers if num != number]
    return count, numbers
number = int(input("Input number: "))
numbers = [2,3,4,23,3,17,10,12,1,2,2,2]
removed, numbers = delnum(numbers,number)
print(removed)
print(numbers)

# Завдання 5
# Напишіть функцію, яка отримує два списки як параметр
# і повертає список з елементами обох списків.

def combaine(list1, list2):
    list3 = list1 + list2
    return list3

list1 = [2,3,3,2,9]
list2 = [3,3,3,3,3,3]
result = combaine(list1, list2)
print(result)

# Завдання 6
# Напишіть функцію, яка підраховує степінь кожного елемента
# списку цілих. Значення для степеня, як і список, передається
# як параметр. Функція повертає новий список з отриманими
# результатами.


def power(list, pow):
    result = []
    for i in range(0, len(list)):
        result.append(list[i]**pow)
    return result

list = [2, 3, 3, 2, 9]
pow = 2
result = power(list, pow)
print(list, result)
