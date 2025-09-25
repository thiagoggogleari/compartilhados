"""
Exercicio 9: Simulando Filtros de Comparação (`__gt`, `__lt`)

Contexto Django:
Django permite filtrar campos numéricos usando lookups de comparação como 
`__gt` (greater than/maior que), `__lt` (less than/menor que), `__gte` 
(greater than or equal/maior ou igual a) e `__lte` (less than or equal/menor 
ou igual a). Ex: `Post.objects.filter(visualizacoes__gte=100)`.

Seu Desafio (Python):
Vamos adicionar uma chave `visualizacoes` aos nossos posts e filtrar com base 
nela.

Escreva uma função `filtrar_posts_por_visualizacoes` que receba a lista de 
posts e um número `min_visualizacoes`. A função deve retornar uma **nova lista** 
contendo apenas os posts que tenham um número de visualizações maior ou igual a 
`min_visualizacoes`.

Exemplo de uso:
```python
posts = [
    {'id': 1, 'titulo': 'Post Popular', 'visualizacoes': 1500},
    {'id': 2, 'titulo': 'Post Novo', 'visualizacoes': 50},
    {'id': 3, 'titulo': 'Post Viral', 'visualizacoes': 10000},
]
posts_populares = filtrar_posts_por_visualizacoes(posts, 1000)
# posts_populares deve conter os posts com id 1 e 3.
```

**Desafio extra:** Modifique a função para que ela também aceite um argumento 
`max_visualizacoes`. A função deve então retornar posts com visualizações entre 
`min_visualizacoes` e `max_visualizacoes`. Se um dos argumentos for `None`, ele 
não deve ser considerado no filtro.
"""

# Coloque sua solução abaixo
