"""
Exercicio 19: Simulando a Resolução de URLs (`reverse`)

Contexto Django:
Para evitar escrever URLs fixas no código (ex: `'/posts/1/'`), o que torna a 
manutenção difícil, o Django usa um sistema de resolução de URLs reversa. A 
função `reverse()` busca um padrão de URL pelo seu nome e preenche os 
parâmetros. Ex: `reverse('post_detail', args=[1])` poderia retornar 
`'/blog/posts/1/'`.

Seu Desafio (Python):
Vamos simular essa funcionalidade.

Você tem um dicionário que mapeia nomes de rotas a padrões de URL. Os padrões 
usam a formatação de string do Python para os parâmetros.
```python
url_map = {
    'lista_posts': '/blog/',
    'post_detalhe': '/blog/post/{}/',         # 1 argumento: id do post
    'posts_por_autor': '/blog/autor/{}/posts/', # 1 argumento: id do autor
}
```

Escreva uma função `gerar_url` que receba o `url_map`, o `nome_da_rota` e uma 
lista de `argumentos`. A função deve encontrar o padrão no mapa e usar os 
argumentos para formatar a string da URL e retorná-la.

Exemplo de uso:
`url1 = gerar_url(url_map, 'post_detalhe', [15])`
`# url1 deve ser '/blog/post/15/'`

`url2 = gerar_url(url_map, 'lista_posts', [])`
`# url2 deve ser '/blog/'`

Se a rota não existir no mapa, a função pode levantar um `KeyError`.

**Dica:** O método de string `.format()` pode receber argumentos de uma lista 
usando o operador splat (`*`). Ex: `'{}'.format(*['a'])`.
"""

# Coloque sua solução abaixo
