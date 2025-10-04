"""
Exercicio 1: Simulando `git init`

Contexto Git/GitHub:
O comando `git init` é o primeiro passo para começar a usar o Git em um projeto. 
Ele cria um novo repositório Git, que é basicamente uma "base de dados" onde 
todas as versões do seu código serão armazenadas. Essa base de dados fica 
escondida em uma pasta chamada `.git`.

Seu Desafio (Python):
Vamos simular a criação dessa "base de dados" do repositório usando um dicionário 
Python.

Escreva uma função chamada `git_init` que não receba nenhum argumento.

A função deve retornar um **novo dicionário** que representará nosso repositório. 
Este dicionário deve ter a seguinte estrutura e valores iniciais:

{
    'arquivos': {},          # Para rastrear os arquivos no último commit
    'area_de_stage': set(),  # Para simular a "Staging Area" (arquivos prontos para commit)
    'commits': []            # Um histórico de todos os commits feitos
}

Este dicionário será a base para os próximos exercícios.
"""

def git_init():
    base = {
            'arquivos': {},
            'area_de_stage': set(),
            'commits': []
            }
    return base

base = git_init()
print(base)



















