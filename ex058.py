'''Melhore o jogo do DESAFIO 028
onde o computador vai "pensar" em um número
 entre 0 a 10. Só que agora o jogador
 vai tantar adivinhar até acartar.
  mostrando no final quantos palpitas
  foram necessários para vencer.'''



from random import randint
computador = randint(0,10)
print (' Olá, eu sou seu computador... \n irei pensar em um número de 0 até 10.')
print('=' *40)
print(' Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input(' Qual o seu palpite? '))
    palpites+=1
    print('='*40)
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print ('Mais... tente novamente.')
        elif jogador > computador:
            print('Menos... jogue novamente.')
            
print(' Acertou com {} tentativas, parabéns!'.format(palpites))