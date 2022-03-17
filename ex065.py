n = 0
p = 'S'
soma = 0 
cont = 0

'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

Aula Anterior
Voltar para Módulo
P'''


while p in 'Ss':
    n = int(input(' Digite um número: '))
    soma+= n
    cont+= 1
    media = soma / cont
    p = str(input (' Deseja continuar? [S/N]')).strip().upper()
    if p not in 'nN' and 'Ss':
        print (' Opção inválida')
print('Foram digitados {} números e a soma deles é {}'.format(cont, soma), end='')
print(' e a medida é {}'.format(media))
    