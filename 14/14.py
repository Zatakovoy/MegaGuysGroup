from collections import Counter


# def calc(x, a, b):
# 	s = ""
# 	x = int(str(x), a)
# 	while x > 0:
# 		s += str(x % b)
# 		x //= b
# 	return s[::-1]


# # 47011
# a = 3*343**8 + 5*49**12 + 7**15 - 49
# print(Counter(calc(a, 10, 7)))
#
#
# # 39243
# b = 4**34 + 5*4**22 + 4**13 + 2*4**9 + 82
# print(len(set(hex(b)[2:])))

# # 47218
# alphabet = "0123456789ABCDE"
#
# for n in alphabet:
# 	a = int("123" + n + "5", 15)
# 	b = int("1" + n + "233", 15)
# 	if (a + b) % 14 == 0:
# 		print(n)
# 		break
#
# answer = (int("12345", 15) + int("14233", 15)) // 14
# print(answer)

# 48381
# alphabet = "0123456789ABCD"
# for k in alphabet:
# 	m = int("8" + k + "12" + k, 14)
# 	n = int("8" + k + "542", 14)
# 	for a in range(1000):
# 		if (m + a) % n == 0:
# 			print(k, a)
# 			break

# from ModuleTest

# def calc(x, a, b):
# 	s = ""
# 	x = int(str(x), a)
# 	while x > 0:
# 		s += str(x % b)
# 		x //= b
# 	return s[::-1]
#
#
# expression = calc(3*216**4 + 2*36**6 - 648, 10, 6)
# print(Counter(expression))
