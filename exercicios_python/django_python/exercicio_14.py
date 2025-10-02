"""
Exercicio 14: Simulando Consultas `OR` com Objetos `Q`

Contexto Django:
Por padrão, múltiplos argumentos no método `.filter()` do Django são combinados 
com um `AND` lógico. `filter(autor='Alice', status='publicado')` busca posts 
ONDE o autor é Alice E o status é publicado.

Para realizar uma consulta com `OR`, o Django utiliza `Q objects`. Exemplo: 
`Post.objects.filter(Q(autor='Alice') | Q(status='rascunho'))` busca posts 
ONDE o autor é Alice OU o status é rascunho.

Seu Desafio (Python):
Vamos simular uma consulta `OR`.

Escreva uma função `buscar_posts_com_condicao_ou` que receba a lista de posts, 
um `termo_titulo` e um `status_desejado`. A função deve retornar uma **nova 
lista** de posts que correspondam a **pelo menos uma** das seguintes condições:
1. O `titulo` do post contém o `termo_titulo` (a busca deve ser case-insensitive).
2. O `status` do post é igual ao `status_desejado`.

Exemplo de uso:
```python
posts = [
    {'titulo': 'Post sobre Python', 'status': 'rascunho'},
    {'titulo': 'Novidades do Django', 'status': 'publicado'},
    {'titulo': 'Outro rascunho', 'status': 'rascunho'},
    {'titulo': 'Dicas de Python', 'status': 'arquivado'},
]

resultado = buscar_posts_com_condicao_ou(posts, 'python', 'publicado')
# O resultado deve conter os posts:
# - 'Post sobre Python' (contém 'python')
# - 'Novidades do Django' (status é 'publicado')
# - 'Dicas de Python' (contém 'python')
```
"""

posts = [
    {'titulo': 'Post sobre Python', 'status': 'rascunho'},
    {'titulo': 'Novidades do Django', 'status': 'publicado'},
    {'titulo': 'Outro rascunho', 'status': 'rascunho'},
    {'titulo': 'Dicas de Python', 'status': 'arquivado'},
    ]

def buscar_posts_com_condicao_ou(posts,titulo,status):
    nova_lista = []
    # Laço percorrendo al ista 
    for i in range(len(posts)):
        # Converte as variáveis para minúsculas para atender o case-insensitive.
        if titulo.lower() in posts[i]['titulo'].lower() or status.lower() in posts[i]['status']:
            nova_lista.append(posts[i])
    
    return nova_lista


res = buscar_posts_com_condicao_ou(posts,'python','publicado')
print(res)






