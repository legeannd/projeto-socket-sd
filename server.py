import socket
import calcEstDesc as calc
import utils

HOST = '127.0.0.1'
PORT = 65433

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:                       
            conn.sendall("digite".encode())
            dados = conn.recv(1024)                           

            dados = utils.strToInt(dados)            

            while True:
                msg = 'menu'.encode()
                conn.sendall(msg)
                escolha = conn.recv(1024)
                escolha = escolha.decode()                            

                if(escolha == '1'):
                    media = calc.media(dados)
                    print(media)
                elif(escolha == '2'):
                    mediana = calc.mediana(dados)
                    print(mediana)                    
                elif(escolha == '3'):
                    moda = calc.moda(dados)
                    print(moda)  
                elif(escolha == '4'):
                    variancia = calc.variancia(dados)
                    print(variancia)  
                elif(escolha == '5'):
                    desvioPadrao = calc.desvioPadrao(dados)
                    print(desvioPadrao)  
                elif(escolha == '6'):
                    calc.distribuicaoDeFrequencia(dados)
                elif(escolha == '7'):
                    exitMessage = str.encode('exit')
                    conn.sendall(exitMessage)
                    conn.close() 
                    s.close()  
                    exit()            
                else:
                    print("Aqui nao porra")     