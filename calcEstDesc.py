import statistics as sts
import numpy as np
import matplotlib.pyplot as plt

def media(dados):
    media = sts.mean(dados)
    return media

def mediana(dados):
    dados = sorted(dados)
    mediana = sts.median(dados)
    return mediana

def moda(dados):
    moda = sts.mode(dados)
    return moda

def distribuicaoDeFrequencia(dados):    
    n_classes = 4
    n_ocorrencias = len(dados)
    frequencias = {'classe1': 0, 'classe2': 0, 'classe3': 0, 'classe4': 0}

    #calculando amplitude
    maior = max(dados)
    menor = min(dados)

    amplitude = maior-menor

    amplitude_classe = round(amplitude/n_classes)

    limites_inf = [menor]
    for i in range(n_classes):
        limites_inf.append(limites_inf[i]+amplitude_classe)
    
    for dado in dados:
        if(dado < limites_inf[1]):
            frequencias['classe1'] +=1
        elif(dado < limites_inf[2]):
            frequencias['classe2'] +=1
        elif(dado < limites_inf[3]):
            frequencias['classe3'] +=1
        elif(dado < limites_inf[4]):
            frequencias['classe4'] +=1          

    #histograma de frequência
    plt.hist(dados, 4)
    plt.xlabel('Classes')
    plt.ylabel('Quantidade')
    plt.title('Ocorrências das Classes')
    plt.grid(True)
    plt.show()

def variancia(dados):        
    variancia = round(np.var(dados), 2)
    return variancia

def desvioPadrao(dados):
    desvioPadrao = round(np.std(dados), 2)
    return desvioPadrao