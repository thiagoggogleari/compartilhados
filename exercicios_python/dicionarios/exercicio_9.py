# Crie um dicionário a partir de duas listas.

lista1 = ["a","b","c","d"]
lista2 = [1,2,3,4,5]

dicio1 = {}
for i in range(len(lista1)):
    dicio1[lista1[i]]= lista2[i]

print(dicio1)
