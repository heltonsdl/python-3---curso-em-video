t = int ( input (' Escolha a tabuada: '))

''' Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.'''


for c in range (0, 11):
    print ('{} x {} = {}'.format(t, c, t * c))