"""
Exercício 10: Combinando Tudo

Escreva um programa que leia números de um arquivo chamado "numeros.txt", um por linha.
O programa deve calcular a soma desses números.

- Use um bloco `try-except` para lidar com `FileNotFoundError`.
- Dentro do `try`, use outro `try-except` para lidar com `ValueError` caso uma linha não contenha um número válido.
- Use um bloco `finally` para garantir que a mensagem "Processamento de arquivo finalizado." seja sempre exibida.
"""

def processar_arquivo_numeros(nome_arquivo):
    # Escreva seu código aqui
    pass

# Para testar, crie um arquivo "numeros.txt" com alguns números e talvez algumas linhas de texto.
# Exemplo de numeros.txt:
# 10
# 20.5
# texto
# 30
#
# Exemplo de uso:
# processar_arquivo_numeros("numeros.txt")