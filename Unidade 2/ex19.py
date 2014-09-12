n = int(input("Digite um numero inteiro maior ou igual que 1: \n"))

def quad(n):
    if n > 1:
        return n**2 + quad(n-1)
    else:
        return 1
print(quad(n))
