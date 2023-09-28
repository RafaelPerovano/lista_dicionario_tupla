alunos = {'bernado': 10, 'marcos': 2.1, 'maria': 7.5, 'mirela':8.9, 'pedro': 6.5}
soma = 0
for nota in alunos.values():
    soma = soma + nota
media = soma / len(alunos)