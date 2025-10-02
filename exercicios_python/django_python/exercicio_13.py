"""
Exercicio 13: Simulando Agregações com Média (`Avg`)

Contexto Django:
Além de contar (`Count`), o Django pode realizar outras operações de agregação 
como `Sum` (soma), `Avg` (média), `Min` (mínimo) e `Max` (máximo). Por exemplo, 
para obter a média de vizualizações de todos os posts: 
`Post.objects.aggregate(media_vizualizacoes=Avg('vizualizacoes'))`.

Seu Desafio (Python):
Vamos calcular a média de vizualizações, mas agrupada por autor.

```python
posts = [
    {'autor_id': 101, 'vizualizacoes': 1500},
    {'autor_id': 102, 'vizualizacoes': 500},
    {'autor_id': 101, 'vizualizacoes': 2500},
    {'autor_id': 102, 'vizualizacoes': 1000},
]
```

Escreva uma função `calcular_media_vizualizacoes_por_autor` que receba a lista 
de posts e um `autor_id` específico. A função deve retornar a **média** de 
vizualizações apenas para os posts daquele autor.

- Se o autor não tiver posts na lista, a função deve retornar 0.
- Lembre-se que média = soma total / quantidade de itens.

Exemplo de uso:
`media_alice = calcular_media_vizualizacoes_por_autor(posts, 101)`
`# media_alice deve ser 2000.0`

`media_bob = calcular_media_vizualizacoes_por_autor(posts, 102)`
`# media_bob deve ser 750.0`

**Dica:** Primeiro, filtre os posts para obter apenas os do autor desejado. 
Depois, calcule a soma das vizualizações e divida pelo número de posts 
encontrados. Cuidado com a divisão por zero!
"""

posts = [
    {'autor_id': 101, 'vizualizacoes': 1500},
    {'autor_id': 102, 'vizualizacoes': 500},
    {'autor_id': 101, 'vizualizacoes': 2500},
    {'autor_id': 102, 'vizualizacoes': 1000},
]

def calcular_media_vizualizacoes_por_autor(posts,autor_id):
    soma_views = 0
    qntd_registros = 0

    for i in range(len(posts)):
        if posts[i]['autor_id'] == autor_id:
            soma_views += posts[i]['vizualizacoes']
            qntd_registros += 1
    try: 
        media = soma_views / qntd_registros
    except ZeroDivisionError:
        return 'Não há registros'
    return media



media_alice = calcular_media_vizualizacoes_por_autor(posts,101)
print("Média Alice: %s"%(media_alice))

media_bob = calcular_media_vizualizacoes_por_autor(posts, 102)
print("Média Bob: %s"%(media_bob))

