from random import choice
from time import sleep
print (' Vamos testar a sua sorte?')
print (' Tente adivinhar em qual número estou pensando...')
número = int (input (' Escreva um número de "0" a "5".'))
if número >=6:
    print('Processando...')
    sleep(2)
    print (' Acho que você não entendeu a brincadeira...')
else:
    lista = choice([0,1,2,3,4,5])
    if lista == número:
        print('Processando...')
        sleep(2)
        print ('Parabéns você acertou!')
    else:
        print ('Processando...')
        sleep(2)
        print ( ' Putz! Não foi dessa vez! =(')
