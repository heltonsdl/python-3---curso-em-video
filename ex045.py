from random import randint
from time import sleep

''' Crie um programa que faça o computador jogar Jokenpô com você.'''


print('''Escolha uma das opções para jogar:
    [0] - Papel
    [1] - Tesoura
    [2] - Pedra''')
print ('='*40)
escolha = int (input (' Digite umas das opções: '))
print (' JO')
sleep(1)
print(' KEN')
sleep(1)
print(' PO!')
print ('='*40)
itens = ('Papel', 'Tesoura', 'Pedra')
computador = randint (0,2)

if computador == 0: # Papel

    if escolha == 1:
        
        print(' Você ganhou!')
        
    elif escolha == 2:
        
        print(' Eu venci!')
    elif escolha == 0:
        
        print(' Empate')
        
    else:
        
        print(' Opção inválida!')
 
    
elif computador == 1: #Tesoura
    
    if escolha == 0:
        
        print(' Eu venci!')
    
    elif escolha == 2:
        
        print(' Você venceu!')
        
    elif escolha == 1:
        
        print(' Empate!')
        
    else:
        
        print(' Opção inválida!')
    
elif computador == 2: # Pedra
    
    if escolha == 1:
        
       print(' Eu venci!')
    
    elif escolha == 3:
        
        print (' Você venceu!')
        
    elif escolha == 2:
        
        print ('Empate!')
        
    else:
         
        print(' Opção inválida!')
        
    
print (' Você jogou {} e eu joguei {}.'.format ( itens[escolha], itens[computador]))

    

