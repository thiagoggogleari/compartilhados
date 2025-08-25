# Crie uma função que recebe uma string e retorna a mesma string invertida.


palavra = input("Insira uma palavra e eu vou inverter ela: ")

def inverte_string(string):
    lista = [] 
    for i in string:
        lista.append(i)
    lista.reverse()
    string_invertida=''.join(lista)
    return string_invertida

print(inverte_string(palavra))
