tempo = int(input("Informe o valor total dos segundos:"))
hora = tempo//3600
minutos = (tempo - hora*3600)//60 
segundos = tempo - (hora*3600 + minutos*60)

if hora < 10 and minutos >= 10 and segundos >= 10:
    print("0",hora,":",minutos,":",segundos)

elif hora < 10 and minutos < 10 and segundos >= 10:
    print("0",hora,":0",minutos,":",segundos)

elif hora < 10 and minutos < 10 and segundos < 10:
    print("0",hora,":0",minutos,":0",segundos)

elif hora < 10 and minutos >= 10 and segundos < 10:
    print("0",hora,":",minutos,":0",segundos)

elif hora >= 10 and minutos >= 10 and segundos < 10:
    print(hora,":",minutos,":0",segundos)

elif hora >= 10 and minutos < 10 and segundos < 10:
    print(hora,":0",minutos,":0",segundos)

elif hora >= 10 and minutos < 10 and segundos >= 10:
    print(hora,":0",minutos,":",segundos)

else:
    print(hora,":",minutos,":",segundos)
input()
