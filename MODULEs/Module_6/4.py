n = [s for s in input("Числа: ").split()]
max_n = -100000
min_n = 100000
max_index = 0
min_index = 0

for i in range(0, len(n)):
    if int(n[i]) > int(max_n):
        max_n = n[i]
        max_index = i
    if int(n[i]) < int(min_n):
        min_n = n[i]
        min_index = i

n[max_index] = min_n
n[min_index] = max_n

print(" ".join(n))