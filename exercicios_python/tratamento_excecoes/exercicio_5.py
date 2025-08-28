"""
Exercício 5: Uso do Bloco `finally`

Escreva um programa que abra um arquivo para escrita, escreva algo nele e, em seguida, feche o arquivo. Use um bloco `finally` para garantir que a mensagem "Tentativa de manipulação de arquivo finalizada." seja sempre impressa, ocorrendo uma exceção ou não.
"""

def escrever_em_arquivo(nome_arquivo, conteudo):
    try:
        arquivo = open(nome_arquivo, 'w')
        arquivo.write(conteudo)
        print("Arquivo escrito com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erro ao manipular o arquivo: {e}")
    finally:
        print("Tentativa de manipulação de arquivo finalizada.")
        try:
            arquivo.close()
        except:
            pass 

escrever_em_arquivo("arquivo_exercício 5.txt", "Arquivo de resolução do exercício 5")