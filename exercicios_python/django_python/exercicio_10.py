"""
Exercicio 10: Simulando Relações (Chave Estrangeira / Foreign Key)

Contexto Django:
Em aplicações reais, os dados são relacionados. Um `Post` é escrito por um 
`Autor`. Em Django, isso é modelado com uma `ForeignKey`. Para acessar os dados 
do autor a partir de um post, a sintaxe é `post.autor.nome`.

Seu Desafio (Python):
Vamos simular essa "junção" de dados. Você receberá duas listas: uma de posts 
e uma de autores.

```python
autores = [
    {'id': 101, 'nome': 'Alice'},
    {'id': 102, 'nome': 'Bob'},
]

posts = [
    {'id': 1, 'titulo': 'Post de Alice', 'autor_id': 101},
    {'id': 2, 'titulo': 'Outro post de Alice', 'autor_id': 101},
    {'id': 3, 'titulo': 'Post do Bob', 'autor_id': 102},
]
```

Escreva uma função `juntar_posts_com_autores` que receba a lista de posts e a 
lista de autores. A função deve retornar uma **nova lista** de posts, onde cada 
dicionário de post foi enriquecido com uma nova chave, `'autor'`, que conterá o 
dicionário completo do autor correspondente.

O resultado esperado para o primeiro post seria:
```python
{
    'id': 1, 
    'titulo': 'Post de Alice', 
    'autor_id': 101, 
    'autor': {'id': 101, 'nome': 'Alice'}
}
```

**Dica:** Para uma solução mais eficiente, você pode primeiro transformar a lista 
de autores em um dicionário onde as chaves são os `id`s dos autores. Isso 
evita percorrer a lista de autores para cada post.
"""

autores = [
    {'id': 101, 'nome': 'Alice'},
    {'id': 102, 'nome': 'Bob'},
]

posts = [
    {'id': 1, 'titulo': 'Post de Alice', 'autor_id': 101},
    {'id': 2, 'titulo': 'Outro post de Alice', 'autor_id': 101},
    {'id': 3, 'titulo': 'Post do Bob', 'autor_id': 102},
]


def juntar_posts_com_autores(posts,autores):

    nova_lista = []

    # Percorre cada registro 'posts'
    for i in range(len(posts)):
        # Captura autor_id de 'posts' 
        autor_id = posts[i]['autor_id']

        # Busca registro do autor na tabela autores.
        autor_atual = ''

        for j in range(len(autores)):
            if autores[j]['id'] == autor_id:
                autor_atual = autores[j]

        # Monta o novo registro de dicionário
        reg_posts = posts[i]
        reg_posts ['autor'] = autor_atual 

        # Atribui a nova lista
        nova_lista.append(reg_posts)
    return nova_lista

novo_dicionario = juntar_posts_com_autores(posts,autores)

print(novo_dicionario)
