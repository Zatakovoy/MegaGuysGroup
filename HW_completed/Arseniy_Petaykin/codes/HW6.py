# Салам уебки! Сегодня порешаем 16-ые задачки.
# Помимо новых задачек, закину еще парочку для повторения (вы сами просили)
# Задание 1
# 5245 (№16 в ЕГЭ)
# def func(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     if n > 2:
#         return 3 * func(n-1) - 2 * func(n-2)
# print(func(7))
# Ответ: 64
# Задание 2
# 4657 (№16 в ЕГЭ)
# def f(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return 2 * g(n-1) + 5 * n
# def g(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return f(n-1) + 2 * n
# print(f(4) + g(4))
# Ответ: 89
# Задание 3
# 33504 (№2 в ЕГЭ)
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if not(((x == (not y)) <= (y and (not z))) or (z and (not w))):
#                     print(x,y,z,w)
# Ответ:wzxy
# Задание 4
# 28542 (№5 в ЕГЭ)
# def calc(x, a, b):
#     s = ''
#     x = int(str(x), a)
#     while x > 0:
#         s += str(x % b)
#         x //= b
#     return s[::-1]
# for n in range(3,1000):
#     r = calc(n, 10, 3)
#     r = r + str(n % 3)
#     result = int(r, 3)
#     if result > 999:
#         print(result)
#         break
# Ответ:1003
# Задание 5
# 37371 (№17 в ЕГЭ)
# counter = 0
# maxx = float('-inf')
# arr = [int(x) for x in open('../files/37371.txt')]
# for i in range(len(arr) - 1):
#     for j in range(i + 1, len(arr)):
#         if (arr[i] - arr[j]) % 60 == 0:
#             counter += 1
#             maxx = max(maxx, (abs(arr[i] - arr[j])))
# print(counter, maxx)
# Ответ:832722 9960
# Extra задание
array = [2, 6, 9, 15, 24, 33, 44, 48, 56, 72, 73, 79, 81, 99, 110, 124]
# def searching(array, iskomoe, start, stop):
#     if start > stop:
#         return False
#     else:
#         mid = (start + stop) // 2
#         if array[mid] == iskomoe:
#             return mid
#         elif array[mid] > iskomoe:
#             return searching(array, iskomoe, start, mid - 1)
#         else:
#             return searching(array, iskomoe, mid + 1, stop)
# start = 0
# stop = len(array)
# iskomoe = 32
# a = searching(array, iskomoe, start, stop)
# if a == False:
#     print('Not found!')
# else:
#     print("Found at index", a)
# Напишите рекурсивный вариант бинарного поиска (поиск элемента в отсортированном массиве)
# Внимательно изучите работу бинарного поиска, чтобы понять как его реализовать
# Я понимаю что скорее всего вы скатаете, но мне пиздец как важно чтоб вы поняли этот алгоритм.
# Это самая база. Прям базовее некуда. Потрените еще заодно понимание рекурсии)))
