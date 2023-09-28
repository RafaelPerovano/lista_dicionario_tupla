numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
pares = []

for n in numeros:
    if n %2 == 0:
        pares.append(n)
        
print('Esses são os numeros pares presentes na tupla: ', pares)