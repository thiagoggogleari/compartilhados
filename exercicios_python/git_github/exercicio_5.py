"""
Exercicio 5: Simulando `git status`

Contexto Git/GitHub:
O comando `git status` é um dos mais úteis. Ele mostra o estado atual do seu 
diretório de trabalho e da Staging Area. Ele informa:
- Quais arquivos foram modificados desde o último commit.
- Quais arquivos estão na Staging Area, prontos para o próximo commit.
- Quais arquivos novos ainda não foram rastreados pelo Git.

Seu Desafio (Python):
Esta é uma simulação mais complexa. Vamos nos concentrar em duas partes: 
arquivos na Staging Area e arquivos novos/modificados.

Escreva uma função `git_status` que receba dois argumentos:
1. O `repositorio`.
2. Um dicionário `diretorio_de_trabalho` que representa os arquivos e seus 
   conteúdos atuais no seu disco (ex: `{'arquivo.py': 'novo conteúdo'}`).

A função deve imprimir:
1. A lista de arquivos que estão na `area_de_stage` (prontos para commitar).
2. A lista de arquivos "modificados": aqueles que estão no `diretorio_de_trabalho` 
   e também no último commit (`repositorio['arquivos']`), mas cujos conteúdos 
   são diferentes.
3. A lista de "arquivos novos": aqueles que estão no `diretorio_de_trabalho` mas 
   não estão no último commit (`repositorio['arquivos']`).

Exemplo:
```python
# Repositório após um commit inicial com 'arquivo.txt'
repo = {
    'arquivos': {'arquivo.txt': 'conteudo antigo'},
    'area_de_stage': {'outro.txt'}, # Adicionado com git_add
    'commits': [...]
}
# Arquivos atuais no disco
trabalho_atual = {
    'arquivo.txt': 'conteudo novo', # Modificado
    'outro.txt': '...',             # Na stage
    'novo_arquivo.log': 'log'       # Novo
}

git_status(repo, trabalho_atual)
```

Saída esperada:
```
Arquivos prontos para commitar:
  - outro.txt

Arquivos modificados:
  - arquivo.txt

Arquivos novos não rastreados:
  - novo_arquivo.log
```
"""

# Coloque sua solução abaixo
