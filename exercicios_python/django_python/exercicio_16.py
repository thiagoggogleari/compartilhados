"""
Exercicio 16: Simulando a Seleção de Campos com `.values()` e `.values_list()`

Contexto Django:
Às vezes, você não precisa de todos os campos de um modelo, apenas de alguns 
dados específicos. Para otimizar, Django oferece:
- `.values('id', 'titulo')`: Retorna uma lista de dicionários, mas cada 
  dicionário contém apenas as chaves `id` e `titulo`.
- `.values_list('titulo', flat=True)`: Retorna uma "lista chata" (flat list) 
  contendo apenas os valores do campo `titulo`, em vez de dicionários.

Seu Desafio (Python):
Implemente essas duas funcionalidades.

**Parte 1: `values`**
Escreva uma função `selecionar_campos` que receba a lista de posts e uma 
lista de nomes de campos (strings). Ela deve retornar uma **nova lista** de 
dicionários, onde cada dicionário contém apenas os campos (chaves) solicitados.

**Parte 2: `values_list`**
Escreva uma função `listar_valores_de_campo` que receba a lista de posts e o 
nome de um único campo. Ela deve retornar uma **lista simples** (ex: `['a', 'b']`) 
contendo apenas os valores daquele campo para cada post.

Exemplo de uso:
```python
posts = [
    {'id': 1, 'titulo': 'Post 1', 'status': 'publicado'},
    {'id': 2, 'titulo': 'Post 2', 'status': 'rascunho'},
]

# Parte 1
dicionarios_simplificados = selecionar_campos(posts, ['id', 'status'])
# Resultado: [{'id': 1, 'status': 'publicado'}, {'id': 2, 'status': 'rascunho'}]

# Parte 2
titulos = listar_valores_de_campo(posts, 'titulo')
# Resultado: ['Post 1', 'Post 2']
```

**Dica:** List comprehensions e dictionary comprehensions tornam a solução 
destes problemas muito concisa e elegante.
"""

import copy

posts = [
    {'id': 1, 'titulo': 'Post 1', 'status': 'publicado'},
    {'id': 2, 'titulo': 'Post 2', 'status': 'rascunho'},
]

# campos = ['id', 'status']
def selecionar_campos(posts,campos):
    # Cria um cópia do dicionário para não alterar os dados originais
    copia_dict = copy.deepcopy(posts) 

    # Percorre os posts do dicionario
    for i in range(len(copia_dict)):
        # Percorre as chaves do registro atual do dicionario
        for chave in list(copia_dict[i].keys()):
            # Se a chave não estiver na lista, ela é removida
            if chave not in campos:
                del copia_dict[i][chave]

    # Retorna a nova lista 
    return copia_dict


def listar_valores_de_campo(posts,chave):
    nova_lista = []
    for i in range(len(posts)):
        nova_lista.append(posts[i][chave])
    return nova_lista
    

dicionarios_simplificados = selecionar_campos(posts, ['id', 'status'])
print("Dicionários Simplificados:\n%s\n"%(dicionarios_simplificados))

valores = listar_valores_de_campo(posts,'titulo')
print("Valores por campo:\n%s\n"%(valores))
