# Crie uma função que recebe um número e verifica se ele é par ou ímpar.

def verificar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

num = int(input("Insira um número: "))

print("O número é %s."%(verificar(num)))
