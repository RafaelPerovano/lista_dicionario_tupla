frutas = {
    'maça': 200,
    'banana': 1080,
    'manga': 100,
    'laranja': 20,
    'pera': 2000,
    'uva': 1800,
}
maior = 0
fruta = ''
for quant in frutas:
    if frutas[quant] > maior:
        maior = frutas[quant]
        fruta = quant
print(fruta, 'É a fruta que está em maior quantidade.')