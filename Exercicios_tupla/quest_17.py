tupla = (('China', 1433783692), ('India', 1366417756), ('Estados Unidos', 326766748), ('Indonesia', 270625567), ('Paquistão', 216565317))
maior = ('' ,0)
tam = len(tupla)
for n in range(tam):
    if tupla[n][1] > maior[1]:
        maior = tupla[n]

print(maior[0],'é o pais mais populoso.')
