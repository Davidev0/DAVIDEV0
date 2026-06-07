compras=[]

while True:
    item=input("Digite um item (ou 'fim' para sair ):")
    if item == "fim":
        break
    compras.append(item)
    print("lista de compras")
    print(compras)