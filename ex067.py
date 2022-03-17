cont = 0
tab = 0
while True:
    tab = int(input('Digite o número para ver a sua tabuada: '))

    while cont <= 10 or p in 'Ss':
        print(f'{tab} x {cont} = {cont * tab}')
        cont += 1
        p = str(input(' Deseja continuar? [S/N]'))
    if tab < 0:
        break
print('Acabou')
