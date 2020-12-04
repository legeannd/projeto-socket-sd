import socket
import calcEstDesc as calc
import utils

HOST = '127.0.0.1'
PORT = 65432

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        resultado = ""

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
                    resultado = "O resultado da média é: "+str(media)
                    conn.sendall(resultado.encode())
                elif(escolha == '2'):
                    mediana = calc.mediana(dados)
                    resultado = "O resultado da mediana é: "+str(mediana)
                    conn.sendall(resultado.encode())
                elif(escolha == '3'):
                    moda = calc.moda(dados)
                    resultado = "O resultado da moda é: "+str(moda)
                    conn.sendall(resultado.encode())
                elif(escolha == '4'):
                    variancia = calc.variancia(dados)
                    resultado = "O resultado da variância é: "+str(variancia)
                    conn.sendall(resultado.encode()) 
                elif(escolha == '5'):
                    desvioPadrao = calc.desvioPadrao(dados)
                    resultado = "O resultado da Desvio Padrão é: "+str(desvioPadrao)
                    conn.sendall(resultado.encode())
                elif(escolha == '6'):
                    calc.distribuicaoDeFrequencia(dados)
                elif(escolha == '7'):
                    exitMessage = str.encode('exit')
                    conn.sendall(exitMessage)
                    conn.close() 
                    s.close()  
                    exit()            
                else:
                    conn.sendall("Mistake".encode())