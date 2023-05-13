# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8


# def exponentiation(basis, power):
#     if power == 1:
#         return basis
#     return basis * exponentiation(basis, power - 1)
#
#
# a = int(input())
# b = int(input())
# print(exponentiation(a, b))


# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
#
# *Пример:*
# 2 2 = 4

# def summa(addend_1, addend_2):
#     if addend_2 < 1:
#         return addend_1
#     return addend_1 + summa(1, addend_2 - 1)
#
# add_1 = int(input())
# add_2 = int(input())
# print(summa(add_1, add_2))