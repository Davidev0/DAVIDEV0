lista_compras=[]
print("==== Bem vindo ao gerenciador de compras ====")
while True:
    item=input("Digite um item para a lista (ou sair para finalizar)")
    if item.lower() == "sair":
       break
    lista_compras.append(item)
    print(f"'{item}' foi adicionado com sucesso")
total_itens=len(lista_compras)
print(f"\n Voce adicionou um total de {total_itens} .")
print("\n sua lista de compras finalizada")
for i, item in enumerate (lista_compras, start = 1):
    print(f"{i}.{item}")
print("Fim do programa")