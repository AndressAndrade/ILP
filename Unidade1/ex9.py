def contagem(L,p):
    c = 0
    for termos in L:
        if termos == p:
            c = c +1
    print("O numero de vezes que o valor desejado aparece na lista e:", c)
L = [1,555,8,7,3,4,5,3,15,5,25,6,7,5,7576] ## o numero 5 aparece 3 vezes
p = 5
contagem(L,p)
input()
