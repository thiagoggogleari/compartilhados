"""
Exercicio 8: Simulando Filtros com `__icontains`

Contexto Django:
Uma das consultas mais poderosas do Django é a de busca textual. Para encontrar 
registros que contenham um determinado pedaço de texto em um campo, de forma 
case-insensitive (ignorando maiúsculas e minúsculas), usa-se o lookup 
`__icontains`. Ex: `Post.objects.filter(titulo__icontains='semana')`.

Seu Desafio (Python):
Sua tarefa é implementar uma função de filtro que simule esse comportamento.

Escreva uma função `filtrar_posts_por_termo` que receba a lista de posts e um 
termo de busca (uma string). A função deve retornar uma **nova lista** contendo 
apenas os posts cujo `titulo` contém o termo de busca. A comparação deve 
ignorar a diferença entre maiúsculas e minúsculas.

Exemplo de uso:
```python
posts = [
    {'id': 1, 'titulo': 'Primeiro Post sobre Python'},
    {'id': 2, 'titulo': 'Rascunho de Ideias em python'},
    {'id': 3, 'titulo': 'Novidades da Semana'},
]
posts_filtrados = filtrar_posts_por_termo(posts, 'python')
# posts_filtrados deve conter os dois primeiros posts.

posts_filtrados_2 = filtrar_posts_por_termo(posts, 'POST')
# posts_filtrados_2 deve conter o primeiro post.
```

**Dica:** Os métodos de string `.lower()` ou `.upper()` são seus melhores amigos 
aqui para garantir que a comparação não seja sensível a maiúsculas/minúsculas.
"""

posts = [
    {'id': 1, 'titulo': 'Primeiro Post sobre Python'},
    {'id': 2, 'titulo': 'Rascunho de Ideias em python'},
    {'id': 3, 'titulo': 'Novidades da Semana'},
]

def filtrar_posts_por_termo(posts,termo):
    termo = termo.lower()
    nova_lista =[]

    for i in range(len(posts)):
        if termo in posts[i]['titulo'].lower() :
            nova_lista.append(posts[i])

    return nova_lista        


# posts_filtrados deve conter os dois primeiros posts.
posts_filtrados = filtrar_posts_por_termo(posts, 'python')
print(posts_filtrados)

# posts_filtrados_2 deve conter o primeiro post.
posts_filtrados_2 = filtrar_posts_por_termo(posts, 'POST')
print(posts_filtrados_2)
