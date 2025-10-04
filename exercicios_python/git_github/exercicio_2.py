"""
Exercicio 2: Simulando `git add`

Contexto Git/GitHub:
Depois de modificar arquivos, o comando `git add <nome_do_arquivo>` é usado para 
adicioná-los à "Staging Area" (Área de Preparação). A Staging Area é um passo 
intermediário onde você agrupa as alterações que farão parte do próximo commit.

Seu Desafio (Python):
Vamos simular a adição de arquivos a essa área.

Escreva uma função chamada `git_add` que receba dois argumentos:
1. O dicionário do `repositorio` (criado no exercício anterior).
2. O `nome_do_arquivo` (uma string) que você deseja adicionar.

A função deve:
1. Adicionar o `nome_do_arquivo` ao `set` que representa a `area_de_stage` no 
   dicionário do repositório.
2. Retornar o dicionário do `repositorio` modificado.

Usar um `set` para a área de stage é ideal porque ele automaticamente cuida de 
evitar nomes de arquivos duplicados.

Exemplo de uso:
```python
meu_repo = git_init() # Função do exercício 1
meu_repo = git_add(meu_repo, 'meu_codigo.py')
meu_repo = git_add(meu_repo, 'leia_me.md')

# O 'area_de_stage' em meu_repo deve ser: {'meu_codigo.py', 'leia_me.md'}
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

meu_repo = git_init() # Função do exercício 1
meu_repo = git_add(meu_repo, 'meu_codigo.py')
meu_repo = git_add(meu_repo, 'leia_me.md')

print(meu_repo)

