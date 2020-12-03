import socket
import calcEstDesc as ced

HOST = '127.0.0.1'  
PORT = 65433

def menu():
    print("---- Calculadora Estatística Descritiva----")
    print("---- Escolha uma opção:                    ")
    print("---- 1) Média      ")
    print("---- 2) Mediana    ")
    print("---- 3) Moda")
    print("---- 4) Variância")
    print("---- 5) Desvio Padrão")
    print("---- 6) Gráfico Distribuição De frequência")

    escolha = input()

    return escolha

while True:    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))  
        
        while True:      
            data = s.recv(1024)
            print(data)

            if(data.decode() == 'exit'):
                s.close()
                exit()
            elif(data.decode() == 'digite'):
                print("Digite os dados a serem calculados separados por ','(ex: 10, 20, 25, 46, 123, 1.200, 23): ")
                dados = input()            
                dados = dados.encode()            
                s.sendall(dados)
            elif(data.decode() == 'menu'):
                escolha = menu()
                s.sendall(escolha.encode())

        
    # print('Received:', repr(data.decode()))