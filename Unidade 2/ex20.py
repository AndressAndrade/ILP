n=int(input("Digite o n-ésimo termo que deseja na sequência de Fibonacci: \n"))

def fibo_rec(n):
    L = []
    if n == 0:
        L = [n]
        return L
    elif n == 1:
        L = fibo_rec(n-1) + [1]
        return L
    else:
        L = fibo_rec(n-1) 
        x = L[-1] + L[-2]
        L += [x]
        return L

print(fibo_rec(n))


def fibo(n):
    if n == 0:
        L = [0]
        return L
    elif n == 1:
        L = [0,1]
        return L
    else:
        ant = 0
        atual = 1
        count = 0
        correcao = n - 1
        L = [0,1]
        while count < correcao:
            prox = ant + atual
            ant = atual
            atual = prox
            L += [prox]
            count += 1
        return L

print(fibo(n))
        
    

