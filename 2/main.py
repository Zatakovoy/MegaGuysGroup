# # 18614
# # ((w → ¬x) ≡ (z → y)) ∧ (y ∨ w).
# print("x y z w")
# for x in range(2):
# 	for y in range(2):
# 		for z in range(2):
# 			for w in range(2):
# 				if (((w <= (not x)) == (z <= y)) and (y or w)) == 1:
# 					print(x, y, z, w)


# 28538
# ((x ∧ y) → (¬z ∨ w)) ∧ ((¬w → x) ∨ ¬y)
# print("x y z w")
# for x in range(2):
# 	for y in range(2):
# 		for z in range(2):
# 			for w in range(2):
# 				if (((x and y) <= ((not z) or w)) and (((not w) <= x) or (not y))) == 0:
# 					print(x, y, z, w)


# from ModuleTest
print("x y z w")
for x in range(2):
	for y in range(2):
		for z in range(2):
			for w in range(2):
				if ((x and y) or (y and z)) == ((x <= w) and (w <= z)):
					print(x, y, z, w)
