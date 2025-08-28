"""
Exercício 7: Múltiplos Blocos `except`

Escreva um programa que peça ao usuário para digitar um número.
Tente converter a entrada para um inteiro e, em seguida, dividir 10 por esse número.
Use múltiplos blocos `except` para tratar `ValueError` e `ZeroDivisionError` de forma diferente.
"""

try:
    numero = int(input("Insira um número: "))
    print("O número %i dividido por 10 é %.2f"%(numero,numero/10))
except(ValueError):
    print("A entrada precisa ser um número inteiro. Verifique.")
except(ZeroDivisionError):
    print("Erro. Não é possível dividir por zero")

