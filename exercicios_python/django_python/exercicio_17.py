"""
Exercicio 17: Simulando Filtros com `__in`

Contexto Django:
Para buscar registros cujo valor de um campo está dentro de uma lista de 
possibilidades, Django usa o lookup `__in`. É o equivalente em banco de dados 
ao operador `in` do Python. Ex: `Post.objects.filter(id__in=[1, 5, 10])` 
busca os posts cujos IDs são 1, 5 ou 10.

Seu Desafio (Python):
Sua tarefa é implementar esse filtro.

Escreva uma função `filtrar_posts_por_lista_de_ids` que receba dois argumentos:
1. A lista de posts.
2. Uma lista de `ids` para buscar.

A função deve retornar uma **nova lista** contendo apenas os posts cujos `id`s 
estão presentes na lista de `ids` fornecida.

Exemplo de uso:
```python
posts = [
    {'id': 1, 'titulo': 'Post 1'},
    {'id': 2, 'titulo': 'Post 2'},
    {'id': 3, 'titulo': 'Post 3'},
    {'id': 4, 'titulo': 'Post 4'},
]

ids_desejados = [1, 3, 5] # 5 não existe
posts_filtrados = filtrar_posts_por_lista_de_ids(posts, ids_desejados)
# posts_filtrados deve conter os posts com id 1 e 3.
```

**Dica de performance:** Para listas de `ids` muito grandes, verificar a 
existência de um item em uma lista (`if item in minha_lista`) pode ser lento. 
É muito mais rápido verificar a existência em um `set` (`if item in meu_set`). 
Converter a lista de `ids` para um `set` no início da sua função pode otimizar 
a busca.
"""

# Coloque sua solução abaixo
