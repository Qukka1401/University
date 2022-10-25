num = int(input())
num_max = num_one = 0
while num != 0:
    num_zero = int(input())
    if num == num_zero:
        num_one += 1
        if num_one > num_max:
            num_max = num_one
    else:
        num_one = 0
    num = num_zero
print(num_max + 1)