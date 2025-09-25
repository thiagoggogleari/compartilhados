"""
Exercicio 20: Simulando Paginação com Slicing

Contexto Django:
QuerySets em Django são "lazy" (preguiçosos). Isso significa que você pode 
pegar uma "fatia" (slice) deles, como em uma lista, para fazer paginação, e o 
Django só buscará no banco de dados os itens daquela fatia. Ex: 
`Post.objects.all()[10:20]` pega o segundo conjunto de 10 posts (a segunda 
página, se a página tiver 10 itens).

Seu Desafio (Python):
Implemente a lógica de paginação usando o fatiamento de listas do Python.

Escreva uma função `paginar_lista` que receba três argumentos:
1. Uma `lista_completa` de itens.
2. O número da `pagina` que se deseja obter (começando da página 1).
3. O `tamanho_da_pagina` (quantos itens por página).

A função deve calcular os índices de início e fim da fatia e retornar a 
sub-lista correspondente à página solicitada.

Exemplo de uso:
```python
lista = list(range(100)) # Uma lista de 0 a 99

# Queremos a página 1, com 10 itens por página
pagina_1 = paginar_lista(lista, 1, 10)
# pagina_1 deve ser [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Queremos a página 3, com 10 itens por página
pagina_3 = paginar_lista(lista, 3, 10)
# pagina_3 deve ser [20, 21, ..., 29]

# E se a última página não estiver completa?
pagina_10 = paginar_lista(lista, 10, 12)
# pagina_10 deve ser [96, 97, 98, 99]
```

**Dica:** Cuidado com os cálculos de índice. O índice de início para a `pagina` 
`p` é `(p - 1) * tamanho_da_pagina`.
"""

# Coloque sua solução abaixo
