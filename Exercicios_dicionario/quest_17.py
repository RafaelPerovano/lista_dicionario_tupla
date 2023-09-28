filmes = {
    "O Poderoso Chefão": 1972,
    "Star Wars: Uma Nova Esperança": 1977,
    "E.T. - O Extraterrestre": 1982,
    "Jurassic Park": 1993,
    "Titanic": 1997,
    "Senhor dos Anéis: A Sociedade do Anel": 2001,
    "Avatar": 2009,
    "A Origem": 2010,
    "Grvidade": 2013,
    "Gravidade": 2012,
    "Parasita": 2019
}
c = 0
ordem = []
tamanho = len(filmes) - 2

while c <= len(filmes) + tamanho:
    maior = 0
    for nomes in filmes:
        if filmes[nomes] > maior:
            maior = filmes[nomes]
            maior_key = nomes
    del filmes[maior_key]
    ordem.append(maior_key)
    c += 1
print(ordem)