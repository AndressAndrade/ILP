L = [2,3,4,5,1]

def perm(X):
    chec =[]
    t = False
    for i in X:
        if i in chec:
            t = True
            break
        elif i <= len(X) and i >= 1:
            chec += [i]
        else:
            t = True
            break
    if not t:
        print("É permutacao")
    else:
        print("Nao é permutacao")
perm(L)



