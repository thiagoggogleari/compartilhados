"""
Exercicio 13: Simulando Agregações com Média (`Avg`)

Contexto Django:
Além de contar (`Count`), o Django pode realizar outras operações de agregação 
como `Sum` (soma), `Avg` (média), `Min` (mínimo) e `Max` (máximo). Por exemplo, 
para obter a média de visualizações de todos os posts: 
`Post.objects.aggregate(media_visualizacoes=Avg('visualizacoes'))`.

Seu Desafio (Python):
Vamos calcular a média de visualizações, mas agrupada por autor.

```python
posts = [
    {'autor_id': 101, 'visualizacoes': 1500},
    {'autor_id': 102, 'visualizacoes': 500},
    {'autor_id': 101, 'visualizacoes': 2500},
    {'autor_id': 102, 'visualizacoes': 1000},
]
```

Escreva uma função `calcular_media_visualizacoes_por_autor` que receba a lista 
de posts e um `autor_id` específico. A função deve retornar a **média** de 
visualizações apenas para os posts daquele autor.

- Se o autor não tiver posts na lista, a função deve retornar 0.
- Lembre-se que média = soma total / quantidade de itens.

Exemplo de uso:
`media_alice = calcular_media_visualizacoes_por_autor(posts, 101)`
`# media_alice deve ser 2000.0`

`media_bob = calcular_media_visualizacoes_por_autor(posts, 102)`
`# media_bob deve ser 750.0`

**Dica:** Primeiro, filtre os posts para obter apenas os do autor desejado. 
Depois, calcule a soma das visualizações e divida pelo número de posts 
encontrados. Cuidado com a divisão por zero!
"""

# Coloque sua solução abaixo
