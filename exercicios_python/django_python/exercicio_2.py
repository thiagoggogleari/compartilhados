"""
Exercicio 2: Simulando a Busca de Objeto Único (`.get()`) 

Contexto Django:
Enquanto `.filter()` retorna uma lista (QuerySet) de objetos, o método `.get()` é 
usado para buscar um **único** registro que corresponda aos critérios. Por exemplo, 
`Post.objects.get(id=1)`.

Uma característica crucial do `.get()` é que ele lança um erro se o objeto não for 
encontrado (`DoesNotExist`) ou se, inesperadamente, mais de um objeto for 
encontrado (`MultipleObjectsReturned`).

Seu Desafio (Python):
Vamos simular esse comportamento de busca e erro com Python puro. Use a lista de 
posts abaixo, que agora inclui um `id` para cada um.

```python
posts = [
    {'id': 1, 'titulo': 'Primeiro Post', 'status': 'publicado'},
    {'id': 2, 'titulo': 'Rascunho de Ideias', 'status': 'rascunho'},
    {'id': 3, 'titulo': 'Post Antigo', 'status': 'arquivado'},
    {'id': 4, 'titulo': 'Novidades da Semana', 'status': 'publicado'},
]
```

Escreva uma função chamada `buscar_post_por_id` que receba a lista de posts e um `id`.

A função deve seguir estas regras:
1. Se encontrar **exatamente um** post com o `id` fornecido, deve retornar o 
   dicionário daquele post.
2. Se **nenhum** post com aquele `id` for encontrado, a função deve levantar (raise) 
   um `ValueError` com a mensagem: f"Post com id={id} não encontrado."
3. Para simular um erro de dados, se por acaso mais de um post tiver o mesmo `id`, 
   a função deve levantar um `ValueError` com a mensagem: f"Múltiplos posts 
   encontrados com id={id}."

"""
posts = [
    {'id': 1, 'titulo': 'Primeiro Post', 'status': 'publicado'},
    {'id': 2, 'titulo': 'Rascunho de Ideias', 'status': 'rascunho'},
    {'id': 3, 'titulo': 'Post Antigo', 'status': 'arquivado'},
    {'id': 4, 'titulo': 'Novidades da Semana', 'status': 'publicado'},
]

def buscar_post_por_id(lista_posts,id):
    registros = []

    for i in range(len(lista_posts)):
        if(lista_posts[i]['id'] == id):
            registros.append(lista_posts[i])
    
#    print(registros)
#    print(len(registros))
    if(len(registros) == 1):
        return registros

    if(len(registros) == 0):
        raise ValueError(f"Post com id = {id} não econtrado.") 

    if(len(registros) > 1):
        raise ValueError(f"Múltiplos posts encontrados com id= {id}")




resultado = (buscar_post_por_id(posts,1))

print("Resultado:\n")
print(resultado)














