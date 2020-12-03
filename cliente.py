import socket

HOST = '127.0.0.1'  
PORT = 65432  

def menu():
    print("---- Calculadora Estatística Descritiva----")
    print("---- Escolha uma opção:                    ")
    print("---- 1) Média      ")
    print("---- 2) Mediana    ")
    print("---- 3) Moda")
    print("---- 4) Variância")
    print("---- 5) Desvio Padrão")
    print("---- 6) Plot Gráfico De frequência")

    escolha = int(input())

    return escolha


while True:
    escolha = menu()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))        
        s.sendall(escolha)
        data = s.recv(1024)
        

    print('Received:', repr(data.decode()))