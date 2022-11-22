lst = [s for s in input('Числа: ').split()]
s = []
for i in range(0, len(lst) - 1):
    if int(lst[i]) < int(lst[i + 1]):
        s.append(lst[i + 1])

print(" ".join(s))