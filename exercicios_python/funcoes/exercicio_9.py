# Crie uma função que recebe uma lista de números e retorna uma nova lista com apenas os números pares.

lista = [1,4,22,66,77,33,2,10]

def retorna_pares(lista_completa):
    lista_pares = []
    for i in range(len(lista_completa)):
        if lista_completa[i] % 2 == 0:
            lista_pares.append(lista_completa[i])
    return lista_pares

print(retorna_pares(lista))