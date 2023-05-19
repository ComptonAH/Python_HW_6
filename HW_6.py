# # Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# # Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d. Каждое число вводится с новой строки.

# first_element = int(input('Enter the first element of the progression: '))
# diff = int(input('Enter the difference of the progression: '))
# count = int(input('Enter the quantity of elements of the progression: '))

# progression = range(1,count+1)
# arithm_prog = [first_element+(index-1)*diff for index in progression]
# print(arithm_prog)


# # Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

# import random

# list = [random.randint(-10,10) for element in range(20)]
# print(list)
# upper_limit = int(input('Enter the upper limit: '))
# lower_limit = int(input('Enter the lower limit: '))
# indexes = []
# i = 0
# for element in list:
#     if element <= upper_limit and element >= lower_limit:
#         indexes.append(i)
#     i += 1
# print(indexes)
