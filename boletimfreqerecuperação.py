print("===== BOLETIM RSCOLAR ======")
n1=float(input("Nota 1 :"))
n2=float(input("Nota 2 :"))
n3=float(input("Nota 3 :"))
n4=float(input("Nota 4 : "))
n5=float(input("Nota 5 :"))
n6=float(input("Nota 6 : "))
n7=float(input("Nota 7 :"))
n8=float(input("Nota 8 :"))
media=(n1+n2+n3+n4+n5+n6+n7+n8)/8
print(f"\nMédia: {media:.1f}")
if media == 10 : 
    print("Perfeito Nota maxima ")
elif media>=9:
    print("Excelente Desempenho")
elif media>=7:
    print("Aprovado !")
elif media>= 5:
    print("Recuperação")
elif media>= 0:
    print("Reprovado")
frequencia = float(input("Frequência (%): "))
print(f"Frequência: {frequencia}%")
if frequencia<75:
    print("Reprovado por falta")
else:
    print("Fim de Bimestre ")

# sistema de recuperação será baseado em 3 questoes de matematica 
print("Faça a recuperação !!!")
acertos=0
r1=int(input("Quanto é 7*3 :"))
if r1 == 15:
    acertos+=1
r2=int(input("Quanto é 2**4" ))
if r2== 16 :
    acertos+=1
r3=int(input("Quanto é 12 ** 3 :"))
if r3 ==1728:
    acertos+=1
else:
    print("nao foi dessa vez ")

