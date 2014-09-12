print("Operacoes disponiveis sao: \n multiplicacao(mult)\n divisao euclidiana(div)\n potencial(pot)\n fatorial(fat)\n logaritmo na base 2(log)")
opera = input("Escreva a abreviacao da operacao desejada: \n")

if opera == 'mult':
    x = int(input("Digite o primeiro valor:"))
    y = int(input("Digite o segundo valor:"))
    r = 0
    p = 0
    if x > 0:
        while x >= 1:
                r = r + y
                x = x-1
        print("O resultado da multiplicacao e:",r)
    elif x < 0 and y > 0:
        while y >= 1:
                r = r + x
                y = y - 1
        print("O resultado da multiplicacao e:",r)
    else:
        x1 = r - x   
        y1 = p - y
        while x1 >= 1:
                r = r + y1
                x1 = x1 - 1
        print("O resultado da multiplicacao e:",r)
    
elif opera == 'fat': 
    x = int(input("Digite o numero:"))
    s = x
    t = x ## essa variavel a mais serve para imprimir o valor inicial de x na saida, pois no 'else', tanto 's' quanto 'x' se modificam ao decorrer do ciclo.
    if x == 0 or x == 1:
        print("O fatorial de",s,"e:",1)
    elif x < 0:
        print("Nao existe fatorial de numero negativo")
    else:          
        while s > 1:
                x = x*(s-1)
                s = s-1
        print("O fatorial de",t,"e:",x)     

elif opera == 'pot':
    x = int(input("Digite a base:"))
    y = int(input("Digite o expoente:"))
    s = x
    t = y 
    if y == 0:
        print("O valor",s,"elevado a",y,"e: 1")
    elif x == 0:
        print("O valor",s,"elevado a",y,"e: 0")
    else:    
        while y > 1:
            x = s*x
            y = y-1
        print("O valor",s,"elevado a",t,"e:",x)

elif opera == 'log':
    x = int(input("Digite o valor do logaritmando:"))
    r = 0
    m = 1
    while x > m:
        m = m*2
        r = r+1
    print("O valor do logaritmo e:",r)
    
elif opera == 'div':
    x = int(input("Digite o dividendo:"))
    y = int(input("Digite o divisor:"))
    r = 0
    if x > 0 and y > 0:
        while x > 0 and x >= y:
            x = x - y
            r = r + 1
        print("O quociente da divisao euclidiana e:",r,"e o resto e:",x)
    else:
        print("Para efetuar esta divisao inclua valores nao-nulos e positivos")
        
else:
    print("Tente novamente com uma das opcoes mencionadas")
input()
    
    













