from random import randint
from time import sleep
print (' Irei pensar em um número de 0 a 5 tente adivinhar...')
print ('-==-' *12)
número = int (input (' Em qual número eu pensei:'))
computador = randint(0, 5) # Sorteia um número
if número == computador:
    print('Processando...')
    sleep(2)
    print (' Parabéns você venceu!')
else:
    print ('Processando...')
    sleep(2)
    print (' Que pena, eu venci!')