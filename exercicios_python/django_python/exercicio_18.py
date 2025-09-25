"""
Exercicio 18: Simulando Filtros de Texto com `__startswith`

Contexto Django:
Similarmente ao `__icontains`, o Django oferece lookups para verificar o início 
ou o fim de uma string. `__startswith` verifica se um campo de texto começa 
com uma determinada string. A versão `__istartswith` faz o mesmo, mas 
ignorando maiúsculas/minúsculas. Ex: 
`User.objects.filter(username__istartswith='a')`.

Seu Desafio (Python):
Implemente o filtro `__istartswith`.

Escreva uma função `filtrar_posts_por_inicio_de_titulo` que receba a lista de 
posts e um `prefixo`. A função deve retornar uma **nova lista** de posts cujos 
títulos começam com o `prefixo` fornecido. A comparação deve ser 
case-insensitive.

Exemplo de uso:
```python
posts = [
    {'id': 1, 'titulo': 'Python é incrível'},
    {'id': 2, 'titulo': 'py-jokes: piadas para programadores'},
    {'id': 3, 'titulo': 'Django vs Flask'},
]

posts_filtrados = filtrar_posts_por_inicio_de_titulo(posts, 'py')
# posts_filtrados deve conter os dois primeiros posts.
```

**Dica:** O método de string `.startswith()` é exatamente o que você precisa. 
Combine-o com `.lower()` para a parte case-insensitive.
"""

# Coloque sua solução abaixo
