# 2. Crie uma lista com 10 números inteiros e exiba a soma deles.

lista = [10,20,30,40,50,40,30,20,10,11]
soma = 0

for i in range(len(lista)):
    soma = soma + lista[i] 

print(soma)