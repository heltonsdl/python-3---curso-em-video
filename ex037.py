num = int (input (' Escreva um número inteiro:'))


'''Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''



print (''' Escolha uma das opções abaixo:
[1] - Conversão para BINÁRIO.
[2] - Conversão para OCTAL.
[3] - Conversão para HEXADECIMAL.''')
opção = int (input (' Escolha uma das opções:'))
if opção == 1:
    print (' A conversão de {} para binário é {}.'.format(num, bin(num)[2:]))
elif opção == 2:
    print(' A conversão de {} para octal é {}.'.format(num, oct(num)[2:]))
elif opção == 3:
    print ('A conversão de {} para hexadecimal é {}.'.format(num, hex(num)[2:]))
else:
    print (' Opção inválida. Tente novamente!')