import math
angulo=float(input("Digite o ângulo em graus :"))
# converter graus para radianos 
rad=math.radians(angulo)
seno=math.sin(rad)
cosseno=math.cos(rad)
tangente=math.tan(rad)
print(f"Seno : {seno:.2f}")
print(f"Cosseno : {cosseno:.2f}")
print(f"Tangente : {tangente:.2f}")