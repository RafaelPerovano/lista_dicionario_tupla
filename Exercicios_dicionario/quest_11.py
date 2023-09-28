paises = {'brasil': 'Brasília', 'japão': 'Toquio','japao': 'Toquio', 'peru': 'Lima', 'italia': 'Roma', 'portugal': 'Lisboa', 'argentina': 'Buenos Aries'}

pais = str(input('Digite uma pais para ver a sua capital: '))

if pais in paises:
    capital = paises[pais]
    print('A capital de {} é {}.'.format(pais, capital))
else:
    print('Esse pais não tem no dicionario.')