# Crie uma função que recebe uma lista de números e retorna a média dos números.

lista = [11,20,60,44,20,7]

def media_lista(lista):
    soma = 0
    for i in range (len(lista)):
        soma = soma + lista[i]
    media = soma / len(lista)
    return media


print("A média dos valores da lista é de %.2f."%(media_lista(lista)))