from math import hypot
'''co = float(input('Escreva o cateto oposto:'))
ca = float(input('Escreva o cateto adjacente:'))
hi = ( co ** 2 + ca ** 2) ** (1/2)
print (' A somas dos catetos é {}.'.format(hi))'''

'''co = float (input( ' Escreva o cateto oposto:'))
ca = float(input('Escreva o cateto adjacente:'))
hi = math.hypot(ca, co)
print (' A somas dos catetos é {:.2f}.'.format(hi))'''

co = float(input(' Escreva o cateto oposto:'))
ca = float(input('Escreva o cateto adjacente:'))
hi = hypot (ca, co)
print ('A somas dos catetos é {:.2f}.'.format(hi))

'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.'''



