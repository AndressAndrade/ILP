from math import sqrt
a = float(input("Digite o valor de a:"))
b = float(input("Digite o valor de b:"))
c = float(input("Digite o valor de c:"))
if a > 0:
	delta = b*b - 4*a*c
	if delta > 0:
		raiz1 = (-b + sqrt(delta))/2*a
		raiz2 = (-b - sqrt(delta))/2*a
		print("As raizes sao",raiz1,"e",raiz2)
	elif delta == 0:
		raiz12 = -b/2*a
		print("As raizes sao identicas:",raiz12)
	else:
		print("Nao tem raizes reais")
