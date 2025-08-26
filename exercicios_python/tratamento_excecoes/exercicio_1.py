"""
Exercício 1: Tratamento de ZeroDivisionError

Escreva uma função que divida dois números. Use um bloco try-except para lidar com a exceção `ZeroDivisionError` que ocorre se o segundo número for zero.
"""

def dividir(a, b):
    try: 
        res = a / b
    except(ZeroDivisionError):
        return "Não é possível dividir por zero!"
    else:
        return res 

print(dividir(10, 2))
print(dividir(10, 0))