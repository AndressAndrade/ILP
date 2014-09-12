n = int(input("Digite o valor 1: \n"))
p = int(input("Digite o valor 2: \n"))
div_n=[]
x = n
div_p=[]
y = p
J = 0
while n > 1:
    if x % n == 0:
        div_n = div_n[:]+[n]
        n = n - 1
    else:
        n = n - 1
while p > 1:
    if y % p == 0:
        div_p = div_p[:]+[p]
        p = p - 1
    else:
        p = p - 1
#primeira parte do codigo serve apenas para gerar a lista de divisores dos numeros colocados
#a segunda parte ira comparar essas duas listas e verificar se são primos
for divisoresn in div_n:
        k = 0
        while k < len(div_p):
            if divisoresn == div_p[k]:
                print("Não são primos")
                J = 1
                break
            else:
                k += 1
               
if k == len(div_p) and not J == 1:
    print("São primos")
input()   
