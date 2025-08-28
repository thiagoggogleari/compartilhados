"""
Exercício 10: Combinando Tudo

Escreva um programa que leia números de um arquivo chamado "numeros.txt", um por linha.
O programa deve calcular a soma desses números.

- Use um bloco `try-except` para lidar com `FileNotFoundError`.
- Dentro do `try`, use outro `try-except` para lidar com `ValueError` caso uma linha não contenha um número válido.
- Use um bloco `finally` para garantir que a mensagem "Processamento de arquivo finalizado." seja sempre exibida.
"""

def processar_arquivo_numeros(nome_arquivo):
    try: 
        # Abrir o arquivo em modo de leitura
        with open('C:/Users/n5687188/codigos/compartilhados/exercicios_python/tratamento_excecoes/numeros.txt', 'r', encoding='utf-8') as arquivo:
            # Ler cada linha do arquivo
            soma_numeros = 0 
            for linha in arquivo:
                # Remover quebras de linha e espaços extras
                linha = linha.strip()
                # Exibir a linha
                print(linha)
                try:
                    soma_numeros = soma_numeros + int(linha)
                except(ValueError):
                    print("Caractere da linha do arquivo não é válido")
        print("A soma dos números presentes no arquivo é de %i"%(soma_numeros))
    except(FileNotFoundError):
        print("Arquivo não encontrado")
    finally:
        print("Processamento de arquivo finalizado.")
processar_arquivo_numeros("numeros.txt")

