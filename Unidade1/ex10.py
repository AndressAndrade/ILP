# 10. Escreva um programa que determine os índices dos elementos máximo e
# mínimo de uma lista de n números inteiros.

lista = [1,14,3,5,2,6]
ord = []
for numero in lista:
    k = 0
    while k < len(ord) and numero > ord[k] :
        k = k + 1
    ord = ord[:k] + [numero] + ord[k:]
print("Menor valor é:",ord[0])
print("Maior valor é:",ord[-1])
input()


    
