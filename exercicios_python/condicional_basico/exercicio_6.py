# 6. Solicite três números ao usuário e exiba o menor deles.

lista = []

num1 = int(input("Insira o primeiro número: "))
lista.append(num1)
num2 = int(input("Insira o segundo número: "))
lista.append(num2)
num3 = int(input("Insira o terceiro número: "))
lista.append(num3)

lista.sort()

print("O menor número inserido é %i."%(lista[0]))

