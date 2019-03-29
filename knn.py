from scipy.io import arff
from io import StringIO
import numpy as np
import math  
NUM_CLASS = 2
KFOLD = 10

f= open("dados.arff")
data, meta = arff.loadarff(f)

def distanciaEuclidiana(i,j):
    cont = 0
    distancia = 0 
    while(cont<len(i)-1):
        distancia = distancia  + pow((i[cont] - j[cont]),2)
        cont = cont +1    
    return math.sqrt(distancia)

def main():
 
    NUM_KNN = [1,2,3,5,7,9,11,13,15]
    
    pontosSelecionados = []
    
    teste = [3,1,1,1,7,19.65,0.4,2.5,7.86,49.13,0.01,2.73,0,0,0,0,5,2,5,2,1,'false']

    
    for x in data:
        print(x)


    
    # #supondo um teste num vetor v_train = data
    # for k in NUM_KNN:
    #     for x in data:
    #         if(len(pontosSelecionados) < k):
    #             pontosSelecionados.append([distanciaEuclidiana(teste,x),x[-1]])
    #         else:
    #             distancia = distanciaEuclidiana(teste,x)
    #             for y in pontosSelecionados:
    #                 if(distancia < y[0]):
    #                     y[0] = distancia
    #                     y[1] = x[-1]
    #                     break

    #     print(pontosSelecionados)
    #     count = 0
    #     distanciaFalse = 0
    #     distanciaTrue = 0
    #     for x in pontosSelecionados:
    #         if(x[1].decode() == 'false'):
    #             if(x[0]==0):
    #                 distanciaFalse = 9999999999999
    #                 break
    #             else:
    #                 distanciaFalse = distanciaFalse + float(1)/x[0]
                
    #             count = count + 1
    #         else:
    #             if(x[0] == 0):
    #                 distanciaTrue = 9999999999999
    #                 break
    #             else:
    #                 distanciaTrue = distanciaTrue + float(1)/x[0]


    #     if( count > len(pontosSelecionados)//2):
    #         print(float(count)/len(pontosSelecionados))
    #         print("Para k = " + str(k) +" sem peso a instancia foi classificada como false",float(count)/len(pontosSelecionados))  
    #     else:
    #         print("Para k = " + str(k) + " sem peso a instancia foi classificada como true",(len(pontosSelecionados) - count)/len(pontosSelecionados)) 
        
    #     if(distanciaFalse > distanciaTrue):
    #         print("Para k = " + str(k) +" com peso a instancia foi classificada como false",distanciaFalse)  
    #     else:
    #         print("Para k = " + str(k) +" com peso a instancia foi classificada como true",distanciaTrue)          
main()