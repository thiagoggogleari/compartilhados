"""
Exercicio 12: Simulando Agregações (`.annotate()` e `Count`)

Contexto Django:
O ORM do Django é poderoso para gerar relatórios. Por exemplo, se você quiser 
contar quantos posts cada autor escreveu, você pode "anotar" a consulta de 
autores com essa contagem: `Autor.objects.annotate(num_posts=Count('post'))`.

Seu Desafio (Python):
Sua tarefa é calcular uma contagem similar usando Python puro.

Usando a lista de posts abaixo, que contém um `autor_id`:
```python
posts = [
    {'id': 1, 'titulo': 'Post de Alice', 'autor_id': 101},
    {'id': 2, 'titulo': 'Outro post de Alice', 'autor_id': 101},
    {'id': 3, 'titulo': 'Post do Bob', 'autor_id': 102},
    {'id': 4, 'titulo': 'Terceiro post de Alice', 'autor_id': 101},
]
```

Escreva uma função `contar_posts_por_autor` que receba a lista de posts. A 
função deve retornar um **dicionário** onde as chaves são os `autor_id`s e os 
valores são a quantidade de posts que cada autor escreveu.

O resultado esperado para o exemplo acima é:
`{101: 3, 102: 1}`

**Dica:** Percorra a lista de posts e use um dicionário para manter a contagem. 
O método `.get(chave, valor_padrao)` de dicionários é muito útil aqui para 
inicializar ou incrementar os contadores.
"""

# Coloque sua solução abaixo
