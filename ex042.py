s1 = int (input (' Digite o primeiro segmento:'))
s2 = int (input (' Digite o segundo segmento:'))
s3 = int (input ( ' Digite o terceiro segmento:'))

'''Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes'''


if s1 < s2 + s3 and s2 < s3 + s1 and s3 < s1 + s2:
    print (' Pode formar um triângulo', end='')
    if s1 == s2 == s3:
        print (' Equilátero!')
    elif s1 != s2 != s3 != s1:
        print (' Escaleno')
    else:
        print (' Isósceles!')