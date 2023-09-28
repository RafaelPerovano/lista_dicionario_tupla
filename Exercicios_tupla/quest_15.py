frutas = ('maçã', 'uva', 'banana', 'morango', 'manga', 'pitaia', 'kiwi')
frutas_usuario = str(input('Digite qual fruta quer saber a posição: '))
n = 0
if frutas_usuario in frutas:
    while n < len(frutas):
        if frutas_usuario == frutas[n]:
            print("sua fruta está na posição ", n)
            break
        n = n + 1
else:
    print('Essa fruta essa não está na lista. ')