numero = int(input("Digite um numero inteiro de 3 digitos:"))
numinvertido = 0
if numero <= 999:
    while numero > 0:
        numinvertido = numinvertido*10 + numero%10
        numero = numero//10
    print("O numero invertido e:",numinvertido)
else:
	print("Tente novamente")	
input()

