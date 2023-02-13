# from functools import lru_cache


# @lru_cache(maxsize=None)
# def factorial(n: int) -> int:
#     if n in [0, 1]:
#         return 1
#     else:
#         return n * factorial(n - 1)
    

# def task45250(n: int) -> int:
#     if n < 3:
#         return 2
#     if n > 2 and n % 2 == 0:
#         return task45250(n - 2) + task45250(n - 1) - n
#     if n > 2 and n % 2 == 1:
#         return task45250(n - 1) - task45250(n - 2) + 2*n


# def task4645(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 3
#     return task4645(n - 1)*n + task4645(n - 2)*(n - 1)


# def task4642(n):
#     if n == 1:
#         return 3
#     return task4642(n - 1) * (n - 1)


# def fibo(n):
#     if n in [1, 2]:
#         return 1
#     return fibo(n - 1) + fibo(n - 2)


# @lru_cache(maxsize=None)
# def KP5996(n):
#     if n < 10:
#         return 0
#     return KP5996(n // 10) + (n // 10 % 10) - (n % 10)


# 2 functions type
# def f(n):
#     if n == 1:
#         return 1
#     return f(n - 1) - n * g(n - 1)
#
#
# def g(n):
#     if n == 1:
#         return 1
#     return f(n - 1) + 2*g(n - 1)



def main():
    # print(task45250(32))
    # print(task4645(5))
    # print(fibo(8))
    print(g(18))
    




if __name__ == "__main__":
    main()
