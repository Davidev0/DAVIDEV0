print("===== BOLETIM RSCOLAR ======")
n1=float(input("Nota 1 :"))
n2=float(input("Nota 2 :"))
n3=float(input("Nota 3 :"))
n4=float(input("Nota 4 : "))
media=(n1+n2+n3+n4)/4
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

