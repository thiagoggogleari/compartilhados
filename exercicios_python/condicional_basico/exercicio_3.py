# 3. Peça ao usuário um número inteiro e informe se ele é par ou ímpar.

num = int(input("Insira um número inteiro: "))

if ((num % 2) == 0):
    print("O número %i é par."%(num))
else:
    print("O número %i é ímpar"%(num))