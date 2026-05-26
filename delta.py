import math
a=int(input("Digite o valor de a : "))
b=int(input("Digite o valor de b : "))
c=int(input("Digite o valor de c : "))
delta=b**2 - 4*a*c
print("o valor de delta e :", delta)
if delta < 0:
    print("A Equação não possui raizes reais . ")
else:
    x1=(-b + math.sqrt(delta))/(2*a)
    x2=(-b + math.sqrt(delta))/(2*a)
    print("x1=", x1)
    print("x2=", x2)