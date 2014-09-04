a = int(input("Digite o valor de a:"))
b = int(input("Digite o valor de b:"))
c = int(input("Digite o valor de c:"))
if a >= b and a >= c:
	if b >= c:
		print(c, b, a)
	else:
		print(b, c, a)
elif c >= b and c >= a:
	if a >= b:
		print(b, a, c)
	else:
		print(a, b, c)
else:
	if a >= c:
		print(c, a, b)
	else:
		print(a, c, b)
