import random
n = 3
m = 6
matrix = [random.randint(0,9)*50 for i in range(m)]
print(matrix)
print("-"*155)
for f in matrix:
    print((f"|{matrix}|")*5)
print("-"*155)

