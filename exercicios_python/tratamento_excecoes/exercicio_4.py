"""
Exercício 4: Uso do Bloco `else`

Modifique o exercício 1 para usar um bloco `else`. O bloco `else` deve ser executado apenas se a divisão for bem-sucedida.
"""

def dividir_com_else(a, b):
    try:
        res = a/b
    except(ZeroDivisionError):
        return "Exceção divisão por zero!"
    else:
        print("Else executado!")
        return res
# Exemplo de uso
print(dividir_com_else(10, 2))
print(dividir_com_else(10, 0))