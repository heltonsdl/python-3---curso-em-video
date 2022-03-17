'''Faça um programa que  leia um número inteiro e digase ele é ou não primo.'''

num = int (input ('Escreva um número: '))
for c in range (1, num + 1):
    print ('{}'.format(c), end=' ')
    if num % c == 0:
        print('\033[33m')
    else:
        print('\033[32m')