#Homework 5

# Завдання 1
# Таблиця множення
num = int(input("Enter a number from 1 to 9: "))
for i in range(1, 10):
    result = i * num
    print(f"{num} * {i} = {result}")
print("End")



# Завдання 2
# Конвертор валют
usd_to_uah = 39.2
eur_to_uah = 43.3
eur_to_usd = 1.10
print("1. UAH\n2. USD\n3. EUR ")
print("Exchange rate:\n\t1 USD = 39.2 UAH\n\t1 EUR = 43.3 UAH\n\t1 EUR = 1,10 USD")
currency_original = int(input("Exchange from (enter 1,2 or 3): "))
if currency_original == 1:
    currency_original_name = "UAH"
elif currency_original == 2:
    currency_original_name = "USD"
elif currency_original == 3:
    currency_original_name = "EUR"
else:
    print("Invalid currency code.")
    exit()

currency_exchange = int(input("Exchange to (enter 1,2 or 3): "))
if currency_exchange == 1:
    currency_exchange_name = "UAH"
elif currency_exchange == 2:
    currency_exchange_name = "USD"
elif currency_exchange == 3:
    currency_exchange_name = "EUR"
else:
    print("Invalid currency code.")
    exit()

amount = float(input("Enter the amount: "))
if currency_original == 1:
    if currency_exchange == 2:
        result = amount/usd_to_uah
    elif currency_exchange == 3:
        result = amount/eur_to_uah
    else:
        result = amount
elif currency_original == 2:
    if currency_exchange == 1:
        result = amount*usd_to_uah
    elif currency_exchange == 3:
        result = amount/eur_to_usd
    else:
        result = amount
elif currency_original == 3:
    if currency_exchange == 1:
        result = amount*eur_to_uah
    elif currency_exchange == 2:
        result = amount*eur_to_usd
    else:
        result = amount
else:
    result = amount
print(f" Operation result: {amount} {currency_original_name} =  {result:.2f} {currency_exchange_name}")




#Завдання 3
# Перевірка на належність числа до вказаного діапазону чисел, вивід всього діапазону з позначенням вказаного числа за допомгою символу "!"

bottom = int(input("Input the bottom: "))
top = float(input("Input the top:"))

while True:
    number = int(input("Input number "))
    if bottom <= number <= top:
        for i in range(int(bottom), int(top) + 1):
            if i == number:
                print(f"!{i}!", end=" ")
            else:
                print(i, end=" ")
        break
    else:
        print(f"{number} is not in the range. Please try again.")
























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

