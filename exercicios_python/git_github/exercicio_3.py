"""
Exercicio 3: Simulando `git commit`

Contexto Git/GitHub:
O comando `git commit -m "Sua mpasensagem"` pega tudo que está na Staging Area e 
cria um "snapshot" permanente (um commit) no seu histórico. Cada commit tem uma 
mensagem que descreve as alterações.

Seu Desafio (Python):
Vamos simular a criação de um commit.

Escreva uma função `git_commit` que receba três argumentos:
1. O `repositorio`.
2. A `mensagem` do commit (uma string).
3. Um dicionário `arquivos_commitados` que representa o estado dos arquivos 
   naquele momento (ex: `{'arquivo.py': 'conteúdo do arquivo'}`).

A função deve:
1. Criar um novo dicionário para representar o commit, contendo a `mensagem` e 
   os `arquivos_commitados`.
2. Adicionar este novo commit à lista de `commits` do repositório.
3. Atualizar os `arquivos` do repositório principal para refletir este último commit.
4. Limpar a `area_de_stage`, pois os arquivos foram commitados.
5. Retornar o `repositorio` atualizado.

Exemplo de uso:
```python
# ... (depois de adicionar arquivos com git_add)
arquivos_atuais = {
    'meu_codigo.py': 'print("Olá Mundo")',
    'leia_me.md': '# Meu Projeto'
}
meu_repo = git_commit(meu_repo, "Commit inicial", arquivos_atuais)

# 'commits' deve ter 1 item, 'area_de_stage' deve estar vazia.
```
"""
import copy 

# Cria um dicionário que representa o repositório
def git_init():
    base = {
            'arquivos': {},
            'area_de_stage': set(),
            'commits': []
            }
    return base

# Adiciona arquivos na área de SET
def git_add(repositorio, nome_arquivo):
    repositorio['area_de_stage'].add(nome_arquivo)
    return repositorio

def git_commit(meu_repo, mensagem, arquivos):
    print("\nCommit a ser inserido:")
    novo_dicio = {}
    novo_dicio['mensagem'] = mensagem
    novo_dicio['arquivos_commitados'] = arquivos
    print(novo_dicio)
    meu_repo['commits'].append(novo_dicio)
    print("\nEtapa de Commit em andamento:")
    print(meu_repo)
    print("\nTransferência da área de stage para arquivos do repositório")
    meu_repo['arquivos'].update(arquivos)  
    print(meu_repo)
    print("\nApagando arquivos da área de stage")
    meu_repo['area_de_stage'].clear()
    print(meu_repo)
#{'arquivos': {}, 'area_de_stage': {'leia_me.md', 'meu_codigo.py'}, 'commits': []}
#    meu_repo['commits'].add(novo_dicio)
    return meu_repo 

meu_repo = git_init() # Função do exercício 1
meu_repo = git_add(meu_repo, 'meu_codigo.py')
meu_repo = git_add(meu_repo, 'leia_me.md')

print("Repositório com arquivos na staging area:")
print(meu_repo)


# Agora, o dicionário de conteúdo corresponde aos arquivos na area_de_stage
arquivos_para_commitar = {
    'meu_codigo.py': 'print("Este é o meu código Python!")',
    'leia_me.md': '# Título do Projeto\nEste é o arquivo LEIA-ME.'
}

# Fazendo o commit com a mensagem e os arquivos corretos
meu_repo = git_commit(meu_repo, "Commit inicial com os primeiros arquivos", arquivos_para_commitar)

print("\nRepositório final, após o commit:")
print(meu_repo)
