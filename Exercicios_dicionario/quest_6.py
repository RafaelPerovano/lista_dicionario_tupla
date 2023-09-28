produtos ={'arroz': 19.90, 'feijão': 7, 'carne': 40, 'pao': 1.20, 'manteiga': 17}
lista_compras = ['arroz', 'feijão', 'carne']
total = 0

for produto in produtos:
    if produto in lista_compras:
        total = total + produtos[produto]

print('O valor total a ser pago é de {}R$ '.format(total))