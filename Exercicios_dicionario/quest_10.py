dicionario = {
    'carro': 'um veículo que se locomove sobre rodas, para transporte de passageiros ou de cargas.',
    'guitarra': 'um instrumento musical semelhante ao violão espanhol comum, de seis cordas simples.',
    'computador': 'uma máquina destinada ao processamento de dados, capaz de obedecer a instruções.',
    'amor': 'uma forte afeição por outra pessoa, nascida de laços de consanguinidade ou de relações sociais.',
    'musica': 'uma combinação harmoniosa e expressiva de sons.',
    'palavra': 'uma manifestação verbal ou escrita formada por um grupo de fonemas com uma significação. '
    }
palavra = str(input('Digite uma palavra para ver a definição: '))
if palavra in dicionario:
    definição = dicionario[palavra]
    print('A definição de {} é {}'.format(palavra, definição))
else:
    print('Essa palavra não tem no dicionario.')