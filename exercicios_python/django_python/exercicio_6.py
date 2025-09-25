"""
Exercicio 6: Simulando Ordenação de QuerySets (`.order_by()`)

Contexto Django:
Uma tarefa muito comum é exibir dados em uma ordem específica. Django facilita 
isso com o método `.order_by()` em um QuerySet. Por exemplo, 
`Post.objects.order_by('titulo')` retornaria todos os posts ordenados 
alfabeticamente por seus títulos.

Seu Desafio (Python):
A sua tarefa é ordenar uma lista de dicionários com base no valor de uma das 
chaves.

Escreva uma função `ordenar_posts_por_campo` que receba dois argumentos:
1. A lista de posts.
2. Uma string com o nome do campo pelo qual a ordenação deve ser feita (ex: 
   `'titulo'` ou `'id'`).

A função deve retornar uma **nova lista** contendo os posts ordenados em ordem 
crescente (de A-Z para strings, do menor para o maior para números). Você pode 
assumir que o campo fornecido para ordenação sempre existirá nos dicionários.

Exemplo de uso:
```python
posts = [
    {'id': 2, 'titulo': 'Rascunho de Ideias'},
    {'id': 4, 'titulo': 'Novidades da Semana'},
    {'id': 1, 'titulo': 'Primeiro Post'},
]
posts_ordenados = ordenar_posts_por_campo(posts, 'titulo')
# O primeiro item em posts_ordenados deve ser o post com id 4.
posts_ordenados_por_id = ordenar_posts_por_campo(posts, 'id')
# O primeiro item em posts_ordenados_por_id deve ser o post com id 1.
```

**Dica:** A função `sorted()` do Python aceita um argumento `key` que é perfeito 
para isso. Vale a pena pesquisar sobre `lambda` functions para usar com a `key`.
"""

# Coloque sua solução abaixo
