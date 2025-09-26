# pylint: disable=unused-variable,comparison-to-True


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
import copy

posts = [
    {'id': 1, 'titulo': 'Título Antigo', 'status': 'publicado'},
    {'id': 2, 'titulo': 'Outro Post', 'status': 'rascunho'},
]

def atualizar_post(posts,id,dados):
    id_encontrada = False
    
    # Procura se tem registro com a mesma id
    for i in range(len(posts)):
        if (posts[i]['id'] == id):
            id_encontrada = True
            break
       
    # Se id_encontrada = True então cria nova lista
    if id_encontrada == True:
        novo_posts = copy.deepcopy(posts)

        # Alterar o registro com valores novos
        for i in range(len(novo_posts)):
            if(novo_posts[i]['id'] == id):
                # Atribui os novos valores
                novo_posts[i]['titulo']=dados['titulo']
                novo_posts[i]['status']=dados['status']
        return(novo_posts) 

    # Se id_encontrada = False, retorna lista antiga
    else:
        return posts




dados = {'status': 'arquivado', 'titulo': 'Título Arquivado'}
nova_lista = atualizar_post(posts, 1, dados)

print(nova_lista)
