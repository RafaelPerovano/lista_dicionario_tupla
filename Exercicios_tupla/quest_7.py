strings = ('o', 'rato', 'roeu', 'a roupa', 'do reii', 'de', 'roma!!!')
palavras = []

for n in strings:
    if len(n) > 5:
        palavras.append(n)
print(palavras)