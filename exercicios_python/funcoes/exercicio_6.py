# Crie uma função que recebe um número e retorna o fatorial desse número.

def fatorial(num):
    if(num < 0):
        return "Não existe fatorial de número negativo" 

    atual = num
    anterior = num - 1
    resultado = 1 

    if(num == 2):
        return 2
    elif(num == 1 or num ==1):
        return 1
    else:
        for i in range(num -2):
            resultado = atual * anterior
            print('%i * %i ='%(atual,anterior),end='')
            atual = resultado 
            anterior = anterior -1
            print(resultado)
    return resultado

try:
    num = int(input("Insira um número para calcular o fatorial: "))
    print(fatorial(num))
except:
    print("Verifique se a entrada é um número inteiro.")