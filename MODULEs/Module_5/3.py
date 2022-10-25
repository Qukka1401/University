x = int(input())
y = int(input())
d = 0
while y>0:
    y = y - x
    x = x + (x//10)
    d += 1
print(d)