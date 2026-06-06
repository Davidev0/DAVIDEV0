def login ():
    usuario_correto="admin"
    senha_correta=12345
    tentativas = 2

    while tentativas > 0 :
        usuario=input("Usuario :")
        senha=int(input("Senha :"))
        if usuario == usuario_correto and senha == senha_correta:
            print("Login Realizado com sucesso !")
            return
        tentativas-=1
        print("Dados incorretos Verifique !")
        login()

