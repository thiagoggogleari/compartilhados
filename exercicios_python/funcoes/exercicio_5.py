# Crie uma função que recebe uma lista de palavras e retorna a palavra mais longa.


lista_palavras = ['batata','sol','estrela','polenta','casca']

def maior_palavra(lista):
    maior = ""
    tamanho = 0

    for i in range(len(lista)):
        if (len(lista[i]) > tamanho):
            tamanho = len(lista[i])
            maior = lista[i]
    return maior

print("A maior palavra é: %s."%(maior_palavra(lista_palavras)))
