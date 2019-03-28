from scipy.io import arff
from io import StringIO
import numpy as np

NUM_CLASS = 2
KFOLD = 10

f= open("dados.arff")
data, meta = arff.loadarff(f)


def main():
    
    print("OI")
    countFalse = 0
    countTrue = 0 
    for x in data:
        if(x[-1].decode() == 'false'):
            countFalse = countFalse +1

        else:
            countTrue = countTrue +1


    print(countFalse)
    print(countTrue)
    ##estratificar a base de dados
    folds = np.asarray([]) 
    print(type(folds))
    print(countFalse//KFOLD)
    print(countTrue//KFOLD)
    
    baseEstratificada = [
        [],[],[],[],[],[],[],[],[],[]

        

    ]
    for i in range(0,KFOLD):
        numFalse = 0
        print(i)
        
        # if(i==0)
        #     print(i)
        #     baseEstratificada.append(1)
        # baseEstratificada[i-1].append(1)

        
        
        for x in data:        
            if(x[-1].decode() == 'false' and numFalse < countFalse//KFOLD ):
                array=np.asarray(x)
                # print(array)
                baseEstratificada[i].append(1)

                numFalse = numFalse + 1
        
                
           
    print(baseEstratificada[0])
    

            
            
    print(numFalse)
main()





