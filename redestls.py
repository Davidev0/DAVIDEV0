import socket
import ssl
host="wwww.google.com"
porta=443
#Cria um contexto TLS seguro
contexto=ssl.create_default_context()
#Conexão TCP 
with socket.create_connection((host, porta)) as sock :#Converte contexto para TLS
    with contexto.wrap_socket(sock, server_hostname=host)as tls:
        print("="* 40)
        print("Conexão TLS Estabelecida !")
        print("="* 40)
        print("Servidor :", host)
        print("Versão TLS :", tls.version())
        print("Criptografia :", tls.cipher())
        certificado=tls.getpeercert()
        print("\nInformações de certificado")
        print("Emitido para:", certificado["subject"])
        print("Emitido por:", certificado["issuer"])