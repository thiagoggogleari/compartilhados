# Crie uma função que recebe uma string e conta o número de vogais na string.

vogais = ['a','e','i','o','u']
palavra = "teste"

def conta_vogal(palavra):
    contagem = 0
    for i in range(len(palavra)):
        if (palavra[i] in vogais):
            contagem = contagem + 1
    return contagem

print("A palavra %s contém %i vogais."%(palavra,conta_vogal(palavra)))