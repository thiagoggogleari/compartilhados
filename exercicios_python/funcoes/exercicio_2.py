# Crie uma função que recebe uma lista de números e retorna o maior número da lista.

lista = [10,2,44,66,80]

def verifica_maior(lista_numeros):
    print(lista_numeros)
    lista_numeros.sort(reverse=True)
    print(lista_numeros)
    return lista[0]

print("O maior número da lista é %i"%(verifica_maior(lista)))



