"""
Exercício 3: Tratamento de FileNotFoundError

Escreva um programa que tente abrir e ler um arquivo chamado "dados.txt". Use um bloco try-except para lidar com a exceção `FileNotFoundError` caso o arquivo não exista.
"""

try:
    with open("dados.txt", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
except(FileNotFoundError):
    print("Exceção \"FileNotFoundError\".")
    print("Arquivo não encontrado")
