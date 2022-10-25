str = input()
s1 = str[:str.find(' ')]
s2 = str[str.find(' ')+1:]
print(s2 + ' ' + s1)
