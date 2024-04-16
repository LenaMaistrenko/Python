# Модуль 15. Модульне тестування
# Тема: Модульне тестування. Частина 1
# Завдання 1
# Створіть клас з набором цілих чисел. Реалізуйте клас з
# такою функціональністю:
# ■ Сума елементів набору;
# ■ Середнє арифметичне елементів набору;
# ■ Максимум елементів набору;
# ■ Мінімум елементів набору.
# Протестуйте усі можливості створеного класу, використовуючи модульне тестування (unittest).

class Number:
    def __init__(self, numbers):
        self.numbers = numbers
    def sum(self):
        return sum(self.numbers)
    def average(self):
        return sum(self.numbers) / len(self.numbers)

    def max(self):
        return max(self.numbers)
    def min(self):
        return min(self.numbers)


import unittest

class TestNumber(unittest.TestCase):

    def test_sum(self):
        num = Number([1, 2, 3, 4, 5])
        self.assertEqual(num.sum(), 15)

    def test_average(self):
        num = Number([1, 2, 3, 4, 5])
        self.assertEqual(num.average(), 3)

    def test_max(self):
        num = Number([1, 2, 3, 4, 5])
        self.assertEqual(num.max(), 5)

    def test_min(self):
        num = Number([1, 2, 3, 4, 5])
        self.assertEqual(num.min(), 1)


if __name__ == '__main__':
    unittest.main()



# Завдання 2
# Створіть клас для числа. Реалізуйте клас з такою функціональністю:
# ■ Запис та читання значення;
# ■ Переведення числа у вісімкову систему числення;
# ■ Переведення числа у шістнадцяткову систему числення;
# ■ Переведення числа у двійкову систему числення.
# Протестуйте усі можливості створеного класу, використовуючи модульне тестування (unittest).
class Number:
    def __init__(self, value):
        self.value = value

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def to_octal(self):
        return oct(self.value)

    def to_hexadecimal(self):
        return hex(self.value)

    def to_binary(self):
        return bin(self.value)

import unittest

class TestNumber(unittest.TestCase):
    def test_set_get_value(self):
        num = Number(42)
        num.set_value(10)
        self.assertEqual(num.get_value(), 10)

    def test_to_octal(self):
        num = Number(42)
        self.assertEqual(num.to_octal(), '0o52')

    def test_to_hexadecimal(self):
        num = Number(42)
        self.assertEqual(num.to_hexadecimal(), '0x2a')

    def test_to_binary(self):
        num = Number(42)
        self.assertEqual(num.to_binary(), '0b101010')

if __name__ == '__main__':
    unittest.main()
