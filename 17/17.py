# Дана числовая последовательность
# Требуется по данному условию: посчитать количество пар и макс/мин (возможную) сумму из этих пар
# Под парами подразумевается: два/три подряд идущих числа или различные элементы (каждый с каждым)


# # 37336
# arr = [int(x) for x in open("37336.txt")]
# count = 0
# # maxx = -10000000000000
# maxx = float("-inf")
# for i in range(len(arr) - 1):
# 	a = arr[i]
# 	b = arr[i + 1]
# 	if (a % 3 == 0) or (b % 3 == 0):
# 		count += 1
# 		maxx = max(maxx, a + b)
# print(count, maxx)

# # 37337
# arr = [int(x) for x in open("37337.txt")]
# # arr = []
# # file = open("37337.txt")
# # for x in file:
# # 	arr.append(int(x))
# count = 0
# maxx = float("-inf")
# for i in range(len(arr)):
# 	for j in range(i + 1, len(arr)):
# 		a = arr[i]
# 		b = arr[j]
# 		if ((a % 160) != (b % 160)) and ((a % 7 == 0) or (b % 7 == 0)):
# 			count += 1
# 			maxx = max(maxx, a + b)
# print(count, maxx)

# 37357
# arr = [int(x) for x in open("37357.txt")]
# count = 0
# maxx = float("-inf")
# for i in range(len(arr)):
# 	for j in range(i + 1, len(arr)):
# 		a = arr[i]
# 		b = arr[j]
# 		if (a + b) % 8 == 0:
# 			count += 1
# 			maxx = max(maxx, a + b)
# print(count, maxx)

# 38951
# arr = [int(x) for x in open("38951.txt")]
# count = 0
# maxx = float("-inf")
# for i in range(len(arr) - 1):
# 	a = arr[i]
# 	b = arr[i + 1]
# 	if ((a % 3 == 0) or (b % 3 == 0)) and ((a + b) % 5 == 0):
# 		count += 1
# 		maxx = max(maxx, a + b)
#
# print(count, maxx)

# Statgrad
arr = [int(x) for x in open("statgrad_17.txt")]
count = 0
maxx_squares = 0
# min_5 = min(list(filter(lambda x: str(x)[-1] == "5", arr)))
min_5 = float("+inf")
for i in range(len(arr)):
	if str(arr[i])[-1] == "5":
		min_5 = min(min_5, arr[i])
# print(min_5)
for i in range(len(arr) - 1):
	a, b = sorted([arr[i], arr[i + 1]])
	if (str(a)[-1] == "5") and (a**2 + b**2) < min_5**2:
		count += 1
		maxx_squares = max(maxx_squares, a**2 + b**2)
print(count, maxx_squares)
