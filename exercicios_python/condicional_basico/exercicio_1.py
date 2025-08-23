# 1. Peça ao usuário um número e informe se ele é positivo, negativo ou zero.

numero = float(input("Insira um número: "))

if(numero > 0):
    print("Número é positivo")
elif(numero < 0):
    print("Número é negativo")
else:
    print("Núero é zero")