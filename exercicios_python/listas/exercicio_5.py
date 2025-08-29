# 5. Crie uma lista com números de 1 a 10 e exiba apenas os pares.

lista = [1,2,3,4,5,6,7,8,9,10]

for i in range(len(lista)):
    if lista[i] % 2 == 0:
        print(lista[i])

