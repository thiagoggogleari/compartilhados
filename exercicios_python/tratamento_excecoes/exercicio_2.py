"""
Exercício 2: Tratamento de ValueError

Escreva um programa que peça ao usuário para digitar um número. Use um bloco try-except para lidar com a exceção `ValueError` que pode ocorrer se a entrada não for um número válido.
"""

try:
    numero = int(input("Insira um númmero: "))
    print("Número: %i"%(numero))
except(ValueError):
    print('Exceção "ValueError"')
    print("Você não inseriu um número.")