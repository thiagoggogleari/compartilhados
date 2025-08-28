"""
Exercício 6: Múltiplas Exceções em um Bloco

Escreva uma função que receba uma lista e um índice. 
Tente acessar o elemento da lista no índice fornecido e dividi-lo por zero.
Use um único bloco `except` para tratar `IndexError` e `ZeroDivisionError`.
"""

def acessar_e_dividir(lista, indice):
    try: 
        return lista[indice] / 0
    except(IndexError):
        print("Exceção. Índice inválido.")
    except(ZeroDivisionError):
        print("Exceção. Divisão por zero.")
    pass

# Exemplo de uso
minha_lista = [1, 2, 3]
acessar_e_dividir(minha_lista, 1)
acessar_e_dividir(minha_lista, 5)