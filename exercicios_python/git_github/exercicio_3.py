"""
Exercicio 3: Simulando `git commit`

Contexto Git/GitHub:
O comando `git commit -m "Sua mensagem"` pega tudo que está na Staging Area e 
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

def git_init():
    base = {
            'arquivos': {},
            'area_de_stage': set(),
            'commits': []
            }
    return base

def git_add(repositorio, nome_arquivo):
    repositorio['area_de_stage'].add(nome_arquivo)
    return repositorio

def git_commit(meu_repo, mensagem, arquivos):
    print()
    print(arquivos)
    pass

meu_repo = git_init() # Função do exercício 1
meu_repo = git_add(meu_repo, 'meu_codigo.py')
meu_repo = git_add(meu_repo, 'leia_me.md')
print(meu_repo)

meu_repo = git_commit(meu_repo, "Commit inicial", arquivos_atuais)

#arquivos_atuais = {
#    'meu_codigo.py': 'print("Olá Mundo")',
#    'leia_me.md': '# Meu Projeto'
#}

