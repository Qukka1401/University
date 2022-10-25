x = int(input())
n = 0
while x>1:
    n += 1
    x //= 2
print(n, 2**n)