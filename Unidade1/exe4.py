a = float(input("Digite o primeiro valor:"))
opera = input("Escolha operacao (+ , - , / , *) :")
b = float(input("Digite o sgundo valor:"))
if opera == '+':
	x = a + b
	print("O resultado e:", x)
elif opera == '-':
	x = a - b
	print("O resultado e:", x)
elif opera == '*':
	x = a * b
	print("O resultado e:", x)
else:
    if b > 0 or b < 0:
        x = a / b
        print("O resultado e:", x)
    else:
        print("Erro. Operacao invalida.")
