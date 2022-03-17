a = float( input(' Qual a altura da parede em metros?'))
c = float ( input(' Qual a largura da parede em metros?'))
mq = a * c
t = mq / 2
print (' Sua parede tem a dimensão de {} x {} e a área de {}m2'.format(a, c,mq))
print (' Será necessário {}litros de tinta.'.format(t))

'''Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.'''