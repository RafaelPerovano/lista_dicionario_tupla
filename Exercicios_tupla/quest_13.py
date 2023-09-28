numeros = (8, 2, 8, 4, 10, 6, 61)
c = 0
for n in numeros:
    if n %2 == 0:
        c += 1
if c == len(numeros):
    print('Todos os numeros são pares.')
else:
    print('Nem todos os numeros são pares.(ou nenhum é)')