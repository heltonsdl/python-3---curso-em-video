from time import sleep
print ('{:=^40}'.format(' \033[01;33m Loja Básica \033[m'))
pg = float (input (' Digite o valor da compra: R$ '))

'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros'''



print('='*40)
print (''' \033[01;34m
  [1] - À vista com dinheiro.
  [2] - À vista com o cartão.
  [3] - Em até 2x sem juros.
  [4] - A partir de 3x com juros de 20%. \033[m''')
print ('='*40)
opção = int (input ( '   Selecione uma das opções: '))  	
print ('=' *40)
print(' PROCESSANDO...')
sleep(1)
if opção == 1:
    dinheiro = pg * (10/100) - pg
    print (' O produto com o valor de R${:.2f} com o pagamento à vista no dinheiro recebe 10% de desconto,saindo por R${:.2f}.'.format(pg, dinheiro * -1))
elif opção == 2:
    cartão1= pg * (5/100) - pg
    print (' O produto com o valor de R${:.2f} com o pagamento à vista no cartão recebe 5% de desconto, saindo por R${:.2f}.'.format(pg, cartão1*-1))
elif opção == 3:
    cartão2 = pg /2
    print (' O produto no valor R${:.2f} pacelado em ate 2 vezes sem juros permanece R${:.2f} com parcelas de R${:.2f}.'.format(pg, pg, cartão2))
elif opção == 4:
    print ('='*40)
    parcelas = int (input (' Em quantas parcelas deseja parcelar?'))
    print ('=' *40)
    print(' CALCULANDO...')
    sleep(2)
    if parcelas <=2:
        print (' Favor selecionar a opção [2]')
    else:
        total = pg * (20/100) + pg
        p = total /parcelas
        print(' O produto no valor de R${:.2f} pacelado em {} vezes irá ter 20% de juros com parcelas de R${:.2f}, e passará para um total de R${:.2f}.'.format(pg, parcelas, p, total))
else:
    print('{:=^40}'.format(' \033[01;31m Opção inválida \033[m '))