вывод = print
ввод = input
a = ввод()
вывод()



def f(a,b,c):
    print(a*b*c) #Функция с заданными параметрами
f(c = 1, a = 4, b = 6)


z = 0
def f(a,b,c):
    z = a * b * c
    print(z)
z = f(1,2,3)
print(z)
#(a) неименнованнный, (b=1)именнованный, *args хранит в себе сколько угодно переменных(неименнованных), **kwags для именнованнных переменных

def f(*args):
    z = 1
    for i in args:
        z *= i
    return z
print(f(1,2,3,5,6))



def f(*args, **kwargs):
    z = 1
    for i in args:
        print(i)
    for j in kwargs:
        print(i, kwargs[j])
f(1,2,3,5,6, x = 2, c = 8)