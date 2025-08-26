"""
Exercício 1: Tratamento de ZeroDivisionError

Escreva uma função que divida dois números. Use um bloco try-except para lidar com a exceção `ZeroDivisionError` que ocorre se o segundo número for zero.
"""

def dividir(a, b):
    try: 
        res = a / b
    except(ZeroDivisionError):
        print("Não é possível dividir por zero!")
    pass

# Exemplo de uso
dividir(10, 2)
dividir(10, 0)