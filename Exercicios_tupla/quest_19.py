numeros = (10, 20, 30, 40, 60, 70, 80, 90)
cont = 0
for n in range(len(numeros)):
    if numeros[n] > 10:
        cont += 1
    
if cont == len(numeros):
    print('Todos os numeros são maiores que 10.')
else:
    print('Nem todos os numeros são maiores que 10.')