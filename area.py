print("===== CALCULADORA DE AREAS")
print("1- Quadrado")
print("2 - Circulo")
print("3 - Triangulo ")
opção=int(input("Escolha a figura  :"))
if opção == 1 : 
    lado=float(input("digite o lado :"))
    area=lado * lado
    print("area do qudrado =", area )
elif opção == 2 :
    b=float(input("Digite a base do triangulo : ")) # b = Base do triângulo
    h=float(input("Digite a altura do triangulo : ")) # h = Altura do triângulo
    area=(b*h)/2
    print("Area do Triângulo =", area)
elif opção == 3 : 
    raio=float(input("Digite o raio :"))
    area=3.14 * (raio * raio)
    print("Area do Circulo", area) # a formula implica que area do circulo = pi.r² ou em situações reais : pi.r²/4
else :
    print("Opção Invalida ")
