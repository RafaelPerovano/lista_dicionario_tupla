gols_jogadores = {
    "Cristiano Ronaldo": 800,
    "Lionel Messi": 750,
    "Neymar Jr.": 400,
    "Robert Lewandowski": 600,
    "Karim Benzema": 550,
    "Kylian Mbappé": 350
}
maior = 0

for nomes in gols_jogadores:
    if gols_jogadores[nomes] > maior:
        maior = gols_jogadores[nomes]
        jogador = nomes
        
print(jogador, 'é o jogador com mais gols.')