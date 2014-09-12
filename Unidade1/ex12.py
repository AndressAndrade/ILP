n = int(input("Digite um valor inteiro e positivo:\n"))
def primomaior(n):
    y = n + 1
    p = y
    c = 0
    j = 0
    while j == 0:
        if c < 2 and y % p == 0:
            c = c + 1
            p = p - 1 
        elif c < 2 and not y % p == 0:
            p = p - 1
        elif c == 2 and p == 0 :
            j = 1
        elif c == 2 and not p == 0:
            y = y + 1
            p = y
            c = 0
    print("O primeiro numero primo, superior a este valor é:",y)
primomaior(n)
input()

