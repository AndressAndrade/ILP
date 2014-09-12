a = int(input("Digite um numero inteiro de 3 digitos: "))
if a <= 999:
	unidade = a%10
	dezena = ((a%100) - unidade)
	centena = a - (a%10)
	numero = ((unidade*100) + dezena + (centena//100))
	print (numero)
else:
	print("Tente novamente")
input()
