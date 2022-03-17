'''Desenvolva um programa que leia o primeiro termo de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.'''

primeiro = int( input('Escreva o primeiro termo: '))
razão = int (input(' Escreva a razão: '))
décimo = primeiro + (10 - 1 ) * razão # enésimo termo de uma PA ( Formula pra calcualr)
for c in range (primeiro, décimo + razão, razão):
    print('{}'.format(c), end='-> ')
print('Fim!')