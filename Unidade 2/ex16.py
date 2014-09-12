lista = [2,5,7,8,4,1]
ord = []
for elemento in lista:
    k = 0
    while k < len(ord) and elemento > ord[k]:
        k = k + 1
    ord = ord[:k]+[elemento]+ord[k:]
print(ord)


