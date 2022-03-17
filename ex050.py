
soma = 0
cont = 0

'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.'''


for c in range (1, 7):
    num = int(input(' Escreva o {}º número: '.format (c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print (' Você informou {} números PARES e a  soma deles  é {}'.format(c, soma))


