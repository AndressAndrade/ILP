def indMax(L):
    indMx = 0
    for i in range(1, len(L)):
        if L[i] > L[indMx]:
            indMx = i
    return indMx

P = [5,2,7,4]

Lord = []
for i in range(len(P)):
    iMax = indMax(P)
    Lord += [ P[iMax] ]
    P[iMax:iMax+1] = []
    K = Lord[::-1]
print(K)

##Linv=[]
##for i in range(len(Lord)):
##    i = Lord[-1]
##    Linv += [i]
##    Lord[len(Lord)-1:] = []
##print (Linv)
