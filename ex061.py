'''Desenvolva um programa que leia o primeiro termo de uma PA.
No final, mostre os 10 primeiros termos dessa progressão. obs: usando o while'''

primeiro = int(input(' Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(' {} -> '.format(termo), end='')
    termo+=razão
    cont += 1
print('FIM!')

