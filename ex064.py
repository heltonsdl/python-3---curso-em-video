cont = n = soma = 0

''' Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''


print (' Digite os valores para soma-los, para parar digite 999:')
n = int(input(' Digite um número: '))
while n != 999:
    soma+= n
    cont+= 1
    n = int(input(' Digite um número: '))
print('A soma dos números digitados é {}'.format(soma), end='')
print (' Total de {} números digitados ----> Fim!'.format(cont))