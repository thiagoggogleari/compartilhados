"""
Exercicio 11: Simulando Relações Múltiplas (Many-to-Many)

Contexto Django:
Outro tipo de relação comum é a `ManyToManyField`. Um `Post` pode ter várias 
`Tags`, e uma `Tag` pode estar em vários `Posts`. Em um objeto de post, as 
tags associadas estariam em `post.tags.all()`.

Seu Desafio (Python):
Vamos simular a busca de posts por uma tag específica.

```python
tags = [
    {'id': 1, 'nome': 'Python'},
    {'id': 2, 'nome': 'Django'},
    {'id': 3, 'nome': 'WebDev'},
]

posts = [
    {'id': 1, 'titulo': 'Intro a Django', 'tags_ids': [2, 3]},
    {'id': 2, 'titulo': 'Funções em Python', 'tags_ids': [1]},
    {'id': 3, 'titulo': 'Desenvolvimento Web com Python', 'tags_ids': [1, 3]},
]
```

Escreva uma função `filtrar_posts_por_tag` que receba a lista de posts, a 
lista de tags e o **nome** de uma tag (ex: 'Python').

A função deve:
1. Encontrar o `id` da tag correspondente ao nome fornecido.
2. Retornar uma **nova lista** contendo apenas os posts que possuem esse `id` em 
   sua lista `tags_ids`.

Se a tag não for encontrada, a função deve retornar uma lista vazia.
"""

# Coloque sua solução abaixo
