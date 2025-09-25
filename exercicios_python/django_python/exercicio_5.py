"""
Exercicio 5: Simulando a Exclusão de um Objeto (`.delete()`)

Contexto Django:
Em Django, para remover um registro do banco de dados, você busca o objeto e 
chama o método `.delete()` nele. Ex: `post = Post.objects.get(id=1)`, 
`post.delete()`.

Seu Desafio (Python):
Sua tarefa é criar uma função que remova um dicionário de uma lista baseando-se 
em seu `id`.

Escreva uma função chamada `deletar_post` que receba dois argumentos:
1. A lista de posts existentes.
2. O `id` do post a ser excluído.

A função deve retornar uma **nova lista** contendo todos os posts, exceto aquele 
com o `id` correspondente. Se nenhum post com o `id` fornecido for encontrado, 
a função deve retornar a lista original sem alterações.

Exemplo de uso:
```python
posts = [
    {'id': 1, 'titulo': 'Post para deletar', 'status': 'publicado'},
    {'id': 2, 'titulo': 'Post para manter', 'status': 'rascunho'},
]
nova_lista = deletar_post(posts, 1)
# nova_lista deve conter apenas o post com id 2.
```

**Dica:** Uma list comprehension pode ser uma forma muito elegante de resolver este 
problema.
"""

# Coloque sua solução abaixo
