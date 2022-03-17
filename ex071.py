from time import sleep

'''Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

cont50 = cont20 = cont10 = cont1 = 0
print(' ------ Simulador de Caixa ------ ')
valor = int(input(' Digite o valor: R$'))
cont50 = cont20 = cont10 = cont5 = cont2 = cont1 = 0
ced50 = 50
ced20 = 20
ced10 = 10
ced5 = 5
ced2 = 2
ced1 = 1
while True:
    if valor >= 50:
        valor-= ced50
        cont50+= 1
    elif valor >= 20:
        valor-= ced20
        cont20+= 1
    elif valor >= 10:
        valor-=ced10
        cont10+=1
    elif valor >= 5:
        valor-=ced5
        cont5+=1 
    elif valor >= 2:
        valor-=ced2
        cont2+=1    
    if valor == 0:
        break
print(' Segue lista de cédulas que serão disponibilizadas...')
sleep(1)
print (f' Nota(s) de R$50:{cont50}\n Nota(s) de R$20: {cont20} \n Nota(s) de R$10: {cont10} \n Nota(s) de R$5: {cont5} \n Nota(s) R$2: {cont2} \n Nota(s) de R$1: {cont1}')
 
    