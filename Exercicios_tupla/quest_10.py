palavras = ('tres', 'tigres', 'tristes', 'para', 'tres', 'pratos', 'de', 'trigo')
tamanho = []
for n in palavras:
    tamanho.append(len(n))

tamanho = tuple(tamanho)
print(tamanho)