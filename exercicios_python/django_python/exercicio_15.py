"""
Exercicio 15: Simulando Comparações entre Campos com Objetos `F`

Contexto Django:
E se você precisar comparar o valor de dois campos no mesmo modelo? Por exemplo, 
encontrar produtos cujo preço de venda é menor que o preço de custo, ou posts 
que foram modificados na mesma data em que foram criados. Para isso, Django 
usa `F expressions`. Ex: 
`Post.objects.filter(data_modificacao__gt=F('data_publicacao'))`.

Seu Desafio (Python):
Vamos simular essa comparação entre campos.

```python
from datetime import datetime, timedelta

posts = [
    {
        'id': 1, 
        'data_publicacao': datetime(2023, 1, 1), 
        'data_modificacao': datetime(2023, 1, 5)
    },
    {
        'id': 2, 
        'data_publicacao': datetime(2023, 2, 10), 
        'data_modificacao': datetime(2023, 2, 10)
    },
    {
        'id': 3, 
        'data_publicacao': datetime(2023, 3, 15), 
        'data_modificacao': datetime(2023, 3, 12) # Modificado ANTES
    },
]
```

Escreva uma função `encontrar_posts_modificados_apos_publicacao` que receba a 
lista de posts. A função deve retornar uma **nova lista** contendo apenas os 
posts cuja `data_modificacao` é estritamente posterior (`>`) à `data_publicacao`.

Para o exemplo acima, o resultado deve conter apenas o post com `id: 1`.

**Dica:** Objetos `datetime` do Python podem ser comparados diretamente usando 
operadores como `>`, `<`, `==`, etc.
"""

from datetime import datetime, timedelta

posts = [
    {
        'id': 1, 
        'data_publicacao': datetime(2023, 1, 1), 
        'data_modificacao': datetime(2023, 1, 5)
    },
    {
        'id': 2, 
        'data_publicacao': datetime(2023, 2, 10), 
        'data_modificacao': datetime(2023, 2, 10)
    },
    {
        'id': 3, 
        'data_publicacao': datetime(2023, 3, 15), 
        'data_modificacao': datetime(2023, 3, 12) # Modificado ANTES
    },
]

def encontrar_posts_modificados_apos_publicacao(posts):
    nova_lista = []

    # Percorre a lista fazendo a comparação
    for i in range(len(posts)):
        if posts[i]['data_modificacao'] > posts[i]['data_publicacao']:
            nova_lista.append(posts[i])
    
    return nova_lista

res = encontrar_posts_modificados_apos_publicacao(posts)
print(res)
