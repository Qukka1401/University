l_1 = [s for s in input().split()]
l_2 = [s for s in input().split()]
l_ans = []

for i in range(0, len(l_1)):
    for j in range(0, len(l_2)):
        if l_1[i] == (l_2[j]):
            l_ans.append(l_1[i])

print(" ".join(l_ans))