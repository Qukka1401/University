a = int(input('введите трехзначное число: '))
s = (a%10) + (a//100) + (a//10%10)
print(s)
