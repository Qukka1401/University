import random
#print(random.randrange(0,6))
print(dir(random)) #показывает содержимое
print(help(random.choice)) #правка о содержимом метода choice

import sys
print(sys.path) #показывает путь(список)

import random as r #подключение модуля random переименного в r
from random import randint as rint, choice as ch
print(rint(1,365))
print(ch())

