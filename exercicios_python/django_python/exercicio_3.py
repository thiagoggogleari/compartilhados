"""
Exercicio 3: Simulando a Criação de uma Instância de Model

Contexto Django:
Para criar um novo registro no banco de dados com Django, normalmente instanciamos 
um objeto do nosso Model e depois chamamos o método `.save()`. Ex: 
`novo_post = Post(titulo="Título", ...)` e `novo_post.save()`. Ao salvar, o Django 
se encarrega de atribuir uma nova chave primária (`id`) ao registro.

Seu Desafio (Python):
Vamos simular a criação de um novo "objeto" post, que será representado como um 
dicionário. Sua função deverá se encarregar de gerar um novo `id`.

Escreva uma função chamada `criar_novo_post` que receba 3 argumentos:
1. A lista de posts já existentes.
2. Uma string para o `titulo` do novo post.
3. Uma string para o `conteudo` do novo post.

A função deve:
1. Calcular o próximo `id` disponível. Uma forma simples é encontrar o `id` mais 
   alto na lista de posts existentes e somar 1. Se a lista estiver vazia, o 
   primeiro `id` deve ser 1.
2. Criar um novo dicionário para o post, que deve conter:
    *   O `id` calculado.
    *   O `titulo` e `conteudo` recebidos como argumento.
    *   Um campo `status` com o valor padrão `'rascunho'`.
3. A função deve retornar apenas o dicionário do post recém-criado. Ela **não** 
   deve modificar a lista de posts original.
"""

import copy 

#novo_post = Post(titulo="Título", ...)
posts = [{'id':1,'titulo':"O verde",'preco':10,'status':'rascunho'},{'id':2,'titulo':"O azul",'preco':15,'status':'rascunho'}]

def criar_novo_post(posts,titulo,conteudo):
    id_maior = 0
    
    # Busca qual é a maior id
    for i in range(len(posts)):
        if posts[i]['id'] > id_maior:
            id_maior = posts[i]['id']

    # Número do próximo registro    
    proximo_id = id_maior + 1
    # Montagem do próximo registro
    registro = {'id':proximo_id,titulo:conteudo,'status':'rascunho'}
    # Cria uma cópia do dicionário
    novo_posts = copy.deepcopy(posts)
    # Adiciona o próximo registro ao novo dicionário 
    novo_posts.append(registro)
    
    return novo_posts


print("Tabela anterior:\n%s\n\n"%(posts))

#Lista de posts, titulo e conteudo 
novo_post = criar_novo_post(posts,'O vermelho',100)

print("Contéudo nova tabela após nova inserção:\n%s"%novo_post)






