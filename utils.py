def strToInt(dados):    
    dados = dados.decode()
        
    dados = dados.split(',')    
    tam = len(dados)    
    
    for i in range(0, tam):        
        dados[i] = dados[i].strip(" ")
        dados[i] = int(dados[i])    
    
    print(dados)
    return dados