l_1 = [s for s in input().split()]
l_2 = [s for s in input().split()]
count = 0

for i in range(0, len(l_1)):
    for j in range(0, len(l_2)):
        if l_1[i] == (l_2[j]):
            count += 1

print(count)