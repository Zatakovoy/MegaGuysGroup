# bin -> 2CC
# oct -> 8CC
# hex -> 16CC
# n *= s  <=> n = n * s
# n /= s  <=> n = n / s
# n %= s  <=> n = n % s
# n **= s  <=> n = n ** s
# n //= s  <=> n = n // s

# 8094
# for n in range(1, 100000):
# 	r = bin(n)[2:]
# 	r += str(r.count("1") % 2)
# 	r += str(r.count("1") % 2)
# 	if int(r, 2) > 43:
# 		print(int(r, 2))

# №27535 (№5 в ЕГЭ) (простое)
# for N in range(2, 1000):
#     R = bin(N)[2:]
#     R = R + R[1] + R[0]
#     R = int(R, 2)
#     if R > 90:
#         print(N)
#         break

# 47209
# for n in range(1, 1000):
# 	r = bin(n)[2:]
# 	digits = list(r)
# 	if digits.count("1") % 2 == 0:
# 		digits.append("0")
# 		digits[0], digits[1] = "1", "0"
# 	elif digits.count("1") % 2 != 0:
# 		digits.append("1")
# 		digits[0], digits[1] = "1", "1"
# 	result = int("".join(digits), 2)
# 	if result > 40:
# 		print(n)
# 		break

# 47209 2nd
# for n in range(1, 1000):
# 	r = bin(n)[2:]
# 	if r.count("1") % 2 == 0:
# 		r = "10" + r[2:] + "0"
# 	elif r.count("1") % 2 != 0:
# 		r = "11" + r[2:] + "1"
# 	result = int(r, 2)
# 	if result > 40:
# 		print(n)
# 		break

# 46963
# for n in range(2, 10000):
# 	s = bin(n)[2:]
# 	count_ones = 0
# 	count_zeros = 0
# 	for i in range(len(s)):
# 		if (i % 2 != 0) and (s[i] == "1"):
# 			count_ones += 1
# 		elif (i % 2 == 0) and (s[i] == "0"):
# 			count_zeros += 1
# 	if abs(count_ones - count_zeros) == 5:
# 		print(n)
# 		break

# 5834 KPolyakov
# from collections import Counter
# for n in range(1_000_000):
# 	s = hex(n)[2:]
# 	if n % 2 == 0:
# 		s += "f"
# 	else:
# 		s += "0"
# 	c = s
#
# 	c = c.replace("a", "10")
# 	c = c.replace("b", "11")
# 	c = c.replace("c", "12")
# 	c = c.replace("d", "13")
# 	c = c.replace("e", "14")
# 	c = c.replace("f", "15")
#
# 	c_sum = sum([int(x) for x in tuple(c)]) % 16
# 	s += hex(c_sum)[2:]
#
# 	g = s
#
# 	g = g.replace("a", "10")
# 	g = g.replace("b", "11")
# 	g = g.replace("c", "12")
# 	g = g.replace("d", "13")
# 	g = g.replace("e", "14")
# 	g = g.replace("f", "15")
#
# 	g_sum = sum([int(x) for x in tuple(g)]) % 16
# 	s += hex(g_sum)[2:]
#
# 	answer = dict(Counter(s))
#
# 	if max(answer.values()) > min(answer.values()) * 5:
# 		print(n)
# 		break

# 15128
# for i in range(9676, 9678):
# 	# s = str(i)
# 	# f_s = int(s[0]) + int(s[1])
# 	digits = [int(x) for x in list(str(i))]  # list comprehension (генератор списка)
# 	# i = 1357 => str(i) = "1357" =>
# 	# list(str(i)) => ["1", "3", "5", "7"]
# 	# int(x) для каждого x из list(str(i)) => digits.append
# 	result = [digits[0] + digits[1], digits[1] + digits[2], digits[2] + digits[3]]
# 	result.remove(min(result))
# 	result.sort()
# 	r = str(result[0]) + str(result[1])
# 	if r == "1315":
# 		print(i)


# Statgrad 2210201
# def sum_bin(x):
# 	return sum([int(i) for i in list(str(x))]) % 2 == 0
#
#
# for n in range(1_000):
# 	r = bin(n)[2:]
# 	if sum_bin(n):
# 		r += "0"
# 	else:
# 		r += "1"
#
# 	a = int(r, 2)
# 	if sum_bin(a):
# 		r += "0"
# 	else:
# 		r += "1"
#
# 	b = int(r, 2)
# 	if sum_bin(b):
# 		r += "0"
# 	else:
# 		r += "1"
#
# 	c = int(r, 2)
#
# 	if c > 1028:
# 		print(n, c)

# from ModuleTest

# for n in range(10000):
# 	r = bin(n)[2:]
# 	r += str(r.count("1") % 2)
# 	r += str(r.count("1") % 2)
# 	result = int(r, 2)
# 	if result > 55:
# 		print(result)