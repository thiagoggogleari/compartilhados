"""
Exercicio 7: Simulando Ordenação Reversa (`.order_by('-campo')`)

Contexto Django:
Para ordenar resultados em ordem decrescente (do maior para o menor, ou de Z-A), 
Django utiliza um prefixo de hífen (`-`) no nome do campo. Por exemplo, 
`Post.objects.order_by('-data_publicacao')` mostraria os posts mais recentes 
primeiro.

Seu Desafio (Python):
Vamos expandir o exercício anterior para suportar ordenação reversa.

Escreva uma função `ordenar_posts` que receba a lista de posts e uma string 
com o campo de ordenação. A lógica deve ser a seguinte:
1. Se a string do campo começar com um hífen (ex: `'-id'`), a ordenação deve 
   ser decrescente.
2. Caso contrário, a ordenação deve ser crescente (comportamento padrão).

A função deve extrair o nome real do campo (removendo o hífen se presente) e 
aplicar a ordenação correta. Retorne uma **nova lista** ordenada.

Exemplo de uso:
```python
posts = [
    {'id': 2, 'titulo': 'Rascunho de Ideias'},
    {'id': 4, 'titulo': 'Novidades da Semana'},
    {'id': 1, 'titulo': 'Primeiro Post'},
]
posts_ordenados = ordenar_posts(posts, '-id')
# O primeiro item em posts_ordenados deve ser o post com id 4.
```

**Dica:** A função `sorted()` também tem um argumento `reverse` (booleano) que 
controla a direção da ordenação.
"""

# Coloque sua solução abaixo
