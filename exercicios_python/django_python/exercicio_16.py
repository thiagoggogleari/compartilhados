"""
Exercicio 16: Simulando a Seleção de Campos com `.values()` e `.values_list()`

Contexto Django:
Às vezes, você não precisa de todos os campos de um modelo, apenas de alguns 
dados específicos. Para otimizar, Django oferece:
- `.values('id', 'titulo')`: Retorna uma lista de dicionários, mas cada 
  dicionário contém apenas as chaves `id` e `titulo`.
- `.values_list('titulo', flat=True)`: Retorna uma "lista chata" (flat list) 
  contendo apenas os valores do campo `titulo`, em vez de dicionários.

Seu Desafio (Python):
Implemente essas duas funcionalidades.

**Parte 1: `values`**
Escreva uma função `selecionar_campos` que receba a lista de posts e uma 
lista de nomes de campos (strings). Ela deve retornar uma **nova lista** de 
dicionários, onde cada dicionário contém apenas os campos (chaves) solicitados.

**Parte 2: `values_list`**
Escreva uma função `listar_valores_de_campo` que receba a lista de posts e o 
nome de um único campo. Ela deve retornar uma **lista simples** (ex: `['a', 'b']`) 
contendo apenas os valores daquele campo para cada post.

Exemplo de uso:
```python
posts = [
    {'id': 1, 'titulo': 'Post 1', 'status': 'publicado'},
    {'id': 2, 'titulo': 'Post 2', 'status': 'rascunho'},
]

# Parte 1
dicionarios_simplificados = selecionar_campos(posts, ['id', 'status'])
# Resultado: [{'id': 1, 'status': 'publicado'}, {'id': 2, 'status': 'rascunho'}]

# Parte 2
titulos = listar_valores_de_campo(posts, 'titulo')
# Resultado: ['Post 1', 'Post 2']
```

**Dica:** List comprehensions e dictionary comprehensions tornam a solução 
destes problemas muito concisa e elegante.
"""

# Coloque sua solução abaixo
