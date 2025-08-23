# 5. Peça ao usuário uma letra e informe se é uma vogal ou consoante.

vogais = ['a','e','i','o','u']
letra = input("Insira uma letra: ")

if(letra.isalpha() == True):
    if (letra in vogais):
        print('A letra é uma vogal.')
    else:
        print('A letra é uma consoante.')
else:
    print('Você não inseriu uma letra!')