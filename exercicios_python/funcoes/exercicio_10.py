# Crie uma função que recebe um número e verifica se ele é um número primo.

def verifica_primo(num):
    
    atual = num 
    anterior = atual - 1
    soma = 0

    if num == 2:
        return "É primo"

    if num < 1:
        return "Não é primo"

    for i in range(num - 2):
        if (atual % anterior) == 0:
            print("Atual: %i"%(atual),end='  ')
            print("Anterior: %i"%(anterior))
            return "Não é primo"
        anterior = anterior - 1
    return "É primo"

entrada = int(input("Insira um número para verificar se ele é primo: "))
print(verifica_primo(entrada))