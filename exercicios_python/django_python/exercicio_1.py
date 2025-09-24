"""
Exercicio 1: Simulando um Filtro de QuerySet

Contexto Django: 
Em Django, para buscar objetos em um banco de dados, usamos QuerySets. 
Um QuerySet é, em essência, uma lista de objetos de um determinado Model (tabela). 
Para filtrar essa lista e encontrar dados específicos, o método .filter() é um dos 
mais utilizados.

Por exemplo, para encontrar todos os posts de um blog com o status "publicado", 
faríamos algo como: Post.objects.filter(status='publicado'). 

O resultado é um novo QuerySet contendo apenas os posts que atendem a essa condição.

Seu Desafio (Python):
O objetivo é simular essa funcionalidade de filtro usando Python puro, focando na 
lógica de iteração e seleção.

Você recebeu a seguinte lista de dicionários, onde cada dicionário representa um 
post de blog:

posts = [
    {'titulo': 'Primeiro Post', 'conteudo': '...', 'status': 'publicado'},
    {'titulo': 'Rascunho de Ideias', 'conteudo': '...', 'status': 'rascunho'},
    {'titulo': 'Post Antigo', 'conteudo': '...', 'status': 'arquivado'},
    {'titulo': 'Novidades da Semana', 'conteudo': '...', 'status': 'publicado'},
]

Escreva uma função em Python chamada `filtrar_posts_por_status` que receba 
dois argumentos:
1. Uma lista de dicionários de posts (como a mostrada acima).
2. Uma string com o status desejado (ex: 'publicado').

A função deve retornar uma **nova lista** contendo apenas os dicionários 
dos posts que correspondem ao status fornecido.
"""

# Coloque sua solução abaixo


posts = [
    {'titulo': 'Primeiro Post', 'conteudo': '...', 'status': 'publicado'},
    {'titulo': 'Rascunho de Ideias', 'conteudo': '...', 'status': 'rascunho'},
    {'titulo': 'Post Antigo', 'conteudo': '...', 'status': 'arquivado'},
    {'titulo': 'Novidades da Semana', 'conteudo': '...', 'status': 'publicado'},
]



def filtrar_posts_por_status(lista_dicio,campo_buscado):
    print("Campo buscado: %s"%(campo_buscado))
    print()

    lista = []
    
    # Verifica a cada dicionário na lista pelo qual o campo status seja igual ao campo buscado.
    for i in range(len(lista_dicio)):
        if lista_dicio[i]['status'] == campo_buscado:
            # Adiciona a lista ao dicionário
            lista.append(lista_dicio[i])
        
    return(lista)



res = filtrar_posts_por_status(posts,'publicado');

print("Resultado:\n%s"%(res))













