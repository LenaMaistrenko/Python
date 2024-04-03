# Задача №1
# Напишіть рекурсивну функцію, яка приймає рядок як аргумент і повертає
# кількість слів у цьому рядку, кількість символів, кількість чисел. Слова у рядку
# відокремлені пробілами. Також напишіть код, який тестує цю функцію на різних рядках.



def count_words_chars_nums(string, in_word=False, words=0, nums=0, chars=0):

    first_char = string[0]

    if first_char == " ":
        return count_words_chars_nums(string[1:], in_word=False, words=words, nums=nums, chars=chars)
    elif first_char.isdigit():
        return count_words_chars_nums(string[1:], in_word=False, words=words, nums=nums + 1, chars=chars + 1)
    else:
        if not in_word:
            words += 1
        return count_words_chars_nums(string[1:], in_word=True, words=words, nums=nums, chars=chars + 1)

strings = [
    "Hello world",
    "aaa bbb cccccc",
    "12345 67890",
    "Hello hello hello"
]

for string in strings:
    words, chars, nums = count_words_chars_nums(string)
    print(f"String: '{string}'")
    print(f"Number of words: {words}")
    print(f"Number of characters: {chars}")
    print(f"Number of numbers: {nums}")

# Задача №2
# Реалізуйте функцію, яка аналізує текст (поданий як рядок) та повертає
# інформацію про кількість унікальних слів, частоту їх використання, та список унікальних
# слів, відсортованих за кількістю їх появи в тексті. Функція має використовувати
# словники для підрахунку частоти та кортежі або множини для зберігання унікальних
# слів. Використовуйте модулі для структурування коду.

def analyze_text(text):
    words = text.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    unique_words = sorted(word_count.keys(), key=lambda word: word_count[word], reverse=True)
    unique_word_count = len(unique_words)

    return unique_word_count, word_count, unique_words


text = "Lorem ipsum dolor sit amet consectetur adipiscing elit consectetur adipiscing Lorem ipsum"
unique_word_count, word_frequency, unique_words = analyze_text(text)

print(f"Number of unique words: {unique_word_count}")
print("Word frequency:")
for word, count in word_frequency.items():
    print(f"{word}: {count}")
print("Unique words sorted by frequency of appearance:")
for word in unique_words:
    print(word)



# Задача №3:
# 1. Створіть параметризований декоратор measure_performance, який може
# приймати булевий аргумент verbose. Якщо verbose встановлено в True, декоратор має
# виводити ім'я функції, час її виконання та результат. Якщо verbose встановлено в False,
# декоратор повинен виводити тільки час виконання.
# 2. Створіть функцію generate_numbers, яка приймає кількість чисел і генерує
# список випадкових чисел цієї довжини. Створіть функцію find_number, яка приймає
# список чисел і число для пошуку, і використовує лінійний пошук, щоб визначити, чи є
# число в списку.
# 3. Застосуйте декоратор measure_performance з різними параметрами verbose
# до обох функцій.

import time
import random

def measure_performance(verbose=True):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time_ns()
            result = func(*args, **kwargs)
            end_time = time.time_ns()
            execution_time = end_time - start_time
            if verbose:
                print(f"Function: {func.__name__}, Execution Time: {execution_time}, Result: {result}")
            else:
                print(f"Execution Time: {execution_time}")
            return result
        return wrapper
    return decorator

@measure_performance(verbose=True)
def generate_numbers(n):
    numbers = [random.randint(1, 10) for _ in range(n)]
    return numbers

@measure_performance(verbose=False)
def find_number(numbers, target):
    for number in numbers:
        if number == target:
            return True
    return False

numbers = generate_numbers(100000)
print("Generated numbers:", numbers)
target_number = 50
print("Target number to find:", target_number)
found = find_number(numbers, target_number)
print("Number found:", found)


