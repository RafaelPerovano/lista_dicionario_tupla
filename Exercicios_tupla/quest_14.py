numeros_tupla = [0, 1, 1, 2, 5, 3, 4, 4, 5]
i = 0
c = 0
numeros = list(numeros_tupla)
while i < len(numeros):
    n = numeros[i]
    c = i + 1
    while c < len(numeros):
        if n == numeros[c]:
            numeros.remove(numeros[c])
        c += 1
    c = 0
    i += 1
numeros_final = tuple(numeros)
print(numeros_final)