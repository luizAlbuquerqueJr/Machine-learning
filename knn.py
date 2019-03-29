from scipy.io import arff
from io import StringIO
import numpy as np

NUM_CLASS = 2
KFOLD = 10

f= open("dados.arff")
data, meta = arff.loadarff(f)


def distanciaEuclidiana(i,j):
    
    # print(i[21])
    
    cont = 0
    distancia = 0 
    while(cont<len(i)-1):
        # print(i[cont],j[cont])
        distancia = distancia  + pow((i[cont] - j[cont]),2)
        cont = cont +1
        
    
    return pow(distancia,1/2)
        

def main():
    # folds = np.asarray([]) 
    # print(type(data))
    # x = np.asarray(data[0])
  
    NUM_KNN = [1,2,3,5,7,9,11,13,15]
    NUM_KNN = [5]
    pontosSelecionados = []
    
    teste = [4,1,1,1,13,39,0.33,3,13,117,0.01,6.5,0,0,0,0,4,4,7,6,1,'false']
    
    teste = [11,3,1,1,49,215.22,0.07,14.67,14.67,3156.61,0.07,175.37,0,0,1,0,12,9,27,22,5,'false']
    #teste = [4,1,1,1,13,39,0.33,3,13,117,0.01,6.5,0,0,0,0,4,4,7,6,1,'false']
    #teste = [3,1,1,1,7,19.65,0.4,2.5,7.86,49.13,0.01,2.73,0,0,0,0,5,2,5,2,1,'false']
    # teste = [12,3,1,1,51,227.43,0.1,10.42,21.83,2369.07,0.08,131.62,0,0,1,0,10,12,26,25,5,'false']
    # teste = [31,4,1,2,141,829.45,0.05,21.52,38.55,17846.19,0.28,991.46,1,19,15,0,27,32,90,51,7,'true']
    # teste = [29,5,1,3,111,641.73,0.08,12.33,52.03,7914.68,0.21,439.7,4,22,27,0,22,33,74,37,9,'true']
    teste = [71,10,8,9,211,1251.39,0.04,27.11,46.15,33930.43,0.42,1885.02,6,45,30,0,26,35,138,73,19,'true']
    # teste = [15,2,1,2,74,385.5,0.07,14.25,27.05,5493.37,0.13,305.19,0,7,9,0,19,18,47,27,3,'true']
     
    #supondo um teste num vetor v_train
    for k in NUM_KNN:
        for x in data:
            if(len(pontosSelecionados) < k):
                pontosSelecionados.append([distanciaEuclidiana(teste,x),x[-1]])
            else:
                distancia = distanciaEuclidiana(teste,x)
                for y in pontosSelecionados:
                    if(distancia < y[0]):
                        y[0] = distancia
                        y[1] = x[-1]
                        break

        print(pontosSelecionados)
        count = 0
        distanciaFalse = 0
        distanciaTrue = 0
        for x in pontosSelecionados:
            if(x[1].decode() == 'false'):
                distanciaFalse = distanciaFalse + float(1)/x[0]
                
                count = count + 1
            else:
                distanciaTrue = distanciaTrue + float(1)/x[0]


        if( count > len(pontosSelecionados)//2):
            print(float(count)/len(pontosSelecionados))
            print("Para k = " + str(k) +" sem peso a instancia foi classificada como false",float(count)/len(pontosSelecionados))  
        else:
            print("Para k = " + str(k) + " sem peso a instancia foi classificada como true",(len(pontosSelecionados) - count)/len(pontosSelecionados)) 
        
        if(distanciaFalse < distanciaTrue):
            print("Para k = " + str(k) +" com peso a instancia foi classificada como false",distanciaFalse)  
        else:
            print("Para k = " + str(k) +" com peso a instancia foi classificada como true",distanciaTrue)  


    
        
main()





