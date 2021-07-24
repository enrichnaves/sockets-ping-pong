import socket

s = socket.socket()
host = "localhost"
port = 12345
print("conectando-se ao servidor")
s.connect((host, port))
print("Conectado")
while True:
    print("Escreva sua mensagem:")
    x = input()
    if x=="SAIR":
        s.close()
        break
    else:
        s.send(x.encode())
        print("Mensagem enviada")
        print("Esperando resposta")
        data = s.recv(1024)
        print("Mensagem recebida:")
        print(data.decode())

