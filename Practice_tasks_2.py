import random
def p():
 for i in range (0,100):
     a = [23,24,25,26,27,28,29,30,31,32] #Количество человек в классе
     c = random.choice(a)
     pc = c*(c-1)/2 #Подсчитывает количество пар

