"""
Exercicio 4: Simulando a Atualização de um Objeto (`.save()`)

Contexto Django:
Para atualizar um registro existente em Django, você primeiro busca o objeto, 
altera seus atributos e depois chama o método `.save()` no mesmo objeto. 
Ex: `post = Post.objects.get(id=1)`, `post.titulo = 'Novo Título'`, `post.save()`.

Seu Desafio (Python):
Vamos simular a atualização de um post em uma lista de dicionários.

Escreva uma função `atualizar_post` que receba três argumentos:
1. A lista de posts existentes.
2. O `id` do post a ser atualizado.
3. Um dicionário (`dados_atualizados`) contendo os novos dados para o post.

A função deve:
1. Procurar na lista o post com o `id` correspondente.
2. Se encontrar, deve criar uma **nova lista** de posts onde o post encontrado 
   está atualizado com os novos dados. Os campos que não estão em 
   `dados_atualizados` devem permanecer inalterados.
3. Se nenhum post com o `id` fornecido for encontrado, a função deve retornar a 
   lista original sem nenhuma modificação.

Exemplo de uso:
```python
posts = [
    {'id': 1, 'titulo': 'Título Antigo', 'status': 'publicado'},
    {'id': 2, 'titulo': 'Outro Post', 'status': 'rascunho'},
]
dados = {'status': 'arquivado', 'titulo': 'Título Arquivado'}
nova_lista = atualizar_post(posts, 1, dados)
# O primeiro post na nova_lista deve ser:
# {'id': 1, 'titulo': 'Título Arquivado', 'status': 'arquivado'}
```
"""

# Coloque sua solução abaixo
