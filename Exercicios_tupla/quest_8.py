numeros = (1, 2, 3, 4, 5, 6,7, 8, 9, 10)
presente = int(input('qual numero deseja verificar se está presente na tupla?(N inteiro) '))
esta = False
for n in numeros:
    if presente == n:
        esta = True
        print('O seu numero {} está presente!'.format(presente))
        break
if esta == False:
    print('O seu numero {} nao está presente...'.format(presente))