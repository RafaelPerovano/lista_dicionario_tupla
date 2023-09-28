estoque = {
    'manteiga': 200,
    'leite': 1080,
    'biscoito': 100,
    'cafe': 20,
    'arroz': 2000,
    'feijao': 1800,
    'queijo': 800,
    'maça': 200,
    'banana': 1080,
    'manga': 100,
    'laranja': 20,
    'pera': 2000,
    'uva': 1800,
}
total = 0
parar = False
print('Se deseja parar digite parar.')

while parar == False:
    item = input('Digite uma refeição usando os itens dessa lista: ')

    if item in estoque:
        total = total + estoque[item]
    elif item == 'parar':
        parar = True
        break
    else:
        print('O item digitado nao esta na lista.')

print('O total das calorias é de ',total, 'calorias.')