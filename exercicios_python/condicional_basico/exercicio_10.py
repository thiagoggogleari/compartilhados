# 10. Solicite ao usuário um número e informe se ele é múltiplo de 3 e de 5 ao mesmo tempo.

num = int(input("Insira um número: "))

if (num % 3 == 0) and (num % 5 == 0):
    print("O número %i é divisível por 3 e 5 ao mesmo tempo"%(num))
else:
    print("O número %i não é divisível por 3 e 5 ao mesmo tempo"%(num))
