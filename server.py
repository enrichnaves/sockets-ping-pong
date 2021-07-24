import socket

s = socket.socket()
host = "localhost"
port = 12345
s.bind((host, port))

s.listen(5)
while True:
   print("Esperando conexão.")
   c, addr = s.accept()
   print("Conectado")
   while(c):
      print("Esperando mensagem")
      try:
         data = c.recv(1024)
         if(len(data)>0):
            print("Mensagem recebida:")
            print(data.decode())
            print("Digite resposta:")
            x = input()
            c.send(x.encode())
         else:
            break
      except:
         break
   print("Conexão Encerrada")
   c.close()