# s = "Grisha Misha Ruslan"
# # slices => <str>[start:stop:step=1]
# print(s[0])  # -> G
# print(s[-1])  # -> n
# print(s[1:4])  # -> ris
# print(s[::2])  # only %2 elements
# print(s[::-1])  # <=> reverse
# print(s[:2])  # first two elements
# print(s[-2:])
# print(s[2::2])
# print(s[2:15:2])
#
# # arr = ["1", "2", "3", "4", "5"]
# # a = "".join(arr)
# # print(a)
#
# s = "arseniy"
# print(len(s))
# # len <=> length

# from math import sqrt
# # Генераторы списков
# arr1 = [i**2 for i in range(1, 11)]
# arr2 = [i**0.5 for i in range(1, 11)]
# arr3 = [i for i in range(1, 11) if i % 2 != 0]
# arr4 = [(2*i - 1) for i in range(1, 11)]
# s = "136548"
# arr5 = [int(i) for i in list(s)]
# заполнить arr квадратами чисел от 1 до 10 вкл.
# for i in range(1, 11):
# 	arr.append(i**2)

# print(help(list))
# print(dir(str))

# arr = [int(x) for x in open("requirements.txt")]
# print(arr[0] + arr[2])

# lambda Функции. Анонимные функции
# def print_hello(name):  # default func
# 	return f"Hello, {name}!"

# func = lambda <var1, var2, ..., var_n>: var1 % 3 == 0
# f = lambda x, y: x % y == 0
# # def f(x):
# # 	return x + 3
# a = 10
# b = 5
# print(f(a, b))
# Функция высшего порядка -
# это функция которая может принимать в качестве аргумента другие функции
# filter, map, reduce
# filter(func, iterable)
# from random import randint
# arr = [randint(-100, 100) for i in range(1000)]
# # def p(x):
# # 	return x % 5 == 0
# #
# # arr_5 = list(filter(p, arr))
# arr_5 = list(filter(lambda x: x % 5 == 0, arr))
# print(arr_5)

# for  # если for-loop не закончился break-ом, то выполняется блок else:
#   ...
# else:
#   ...

# if <лог.выражение>:
