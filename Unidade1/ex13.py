n = int(input("Digite um numero inteiro positivo:\n"))
num_per = []
while n > 1:
    x = n - 1
    y = n - 1 ## tem que sem menores que o numero colocado
    div_n=[]
    soma = 0
    c = 0
    while y >= 1:
        if x % y == 0:
            div_n = div_n[:]+[y]  
            y = y - 1
        else:
            y = y - 1
    while c < len(div_n):
        soma = soma + div_n[c]
        c = c + 1
    if soma == 2 * x:
        num_per = num_per[:] + [x]
        n = n - 1
    else:
        n = n - 1
print("A lista de numeros perfeitos menor que o numero digitado é:",num_per)
input()    
