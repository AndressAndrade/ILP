a = float(input("Digite o valor de a:"))
b = float(input("Digite o valor de b:"))
c = float(input("Digite o valor de c:"))
if a > 0 and b > 0 and c > 0:
	if a < b + c and b < a + c and c < a + b:
		perimetro = a + b + c
		print("O perimetro do triangulo e:", perimetro)
	else:
		print("Nao e triangulo")
