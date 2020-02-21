from math import *
n = input("Введите диапазон:- ")
p = [2,3]
count = 2
a = 5
while(cout < n):
    b = 0
    for i in range(2,a):
        if (i <= sqrt(a)):
            if(a % 1 == 0):
                print("не простое число", a)
                b = 1
            else:
                pass
    if (b != 1):
        print("простое число", a)
        p = p+[a]
    count += 1
    a += 2
print p
