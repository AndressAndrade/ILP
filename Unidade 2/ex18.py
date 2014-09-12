##L = [5,8,4,1,5,89,12,34,2,9,10,67] 
##def maiore(X): 
##    if len(X) > 1: 
##        orde = [] 
##        for elemento in X: 
##            k = 0
##            while k < len(orde) and elemento > orde[k]: 
##                k = k + 1
##            orde[k:k] = [elemento] 
##        orde[0:1]=[] 
##        X = orde 
##        maiore(X) 
##    else: 
##        print(X) 
##   
##maiore(L) 

L = [5,8,4,1,5,89]

def n(X):
    if len(X) > 1: # se  a lista tem comprimento maior que 1
        if X[0] > X[1]: #ve se a posicao 0 é maior que a 1
            X = [X[0]]+ X[2:] # como a posicao 0 é maior que a 1, elimina a 1
            n(X) 
        else:
            X = X[1:]# se a posicao 1 é maior que a 0, elimina a 0
            n(X) 
    else:
        print(X)#Quando houver apenas um elemento, imprime esse elemento

n(L)
    
