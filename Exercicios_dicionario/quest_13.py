estoque = {
    'manteiga': 200,
    'leite': 1080,
    'biscoito': 100,
    'cafe': 20,
    'arroz': 2000,
    'feijao': 1800,
    'queijo': 800
}
valor = 1000
abaixo = []

for produtos in estoque:
    if estoque[produtos] < valor:
        abaixo.append(produtos)
print(abaixo, 'Esses itens estão abaixo do valor.')