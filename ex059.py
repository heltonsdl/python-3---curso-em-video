from time import sleep
quest = 0

'''Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''


    
n1 = int(input(' Digite um número: '))
n2 = int(input(' Digite outro número: '))
while not quest == 5:
    print('='*40)
    print('''     [1] - SOMA
     [2] - MULTIPLICAR
     [3] - MAIOR
     [4] - NOVOS NÚMEROS
     [5] - SAIR DO PROGRAMA''')
    print('='*40)
    quest = int (input(' O que deseja fazer? '))
    if quest == 1:
        print('='*40)
        soma = n1 + n2
        print ('  {} + {} = {}'.format(n1, n2, soma))
        print('='*40)
    elif quest == 2:
        print('='*40)
        produto = n1 * n2
        print('  {} x {} = {}'.format(n1, n2, produto))
        print('='*40)
    elif quest == 3:
        
        if n1 > n2:
            print('='*40)
            print(' O maior dentre os números digitados é {}.'.format(n1))
            print('='*40)
        
        else:
            print(' O maior dentres os números digitados é {}.'.format(n2))
    elif quest == 4:
        
        print(' Reiniciando...')
        sleep(1)
        n1 = int(input(' Digite um número: '))
        n2 = int(input(' Digite outro número: '))
        print ('='*40)
        
    elif quest == 5:
     
        print(' Finalizando...')
        sleep(1)
        print(' Obrigado, volte sempre!')
    else:
        print (' Opção inválida, tente novamente!')