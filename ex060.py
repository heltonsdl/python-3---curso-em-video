from math import factorial
n = int(input(' Digite um número para descobrir o seu fatorial: '))
c = n
f = factorial (n)
print('=-='*12)
print('Calculando {}! = '.format(n), end='')
while c > 0:

    print('{} '.format(c), end='')
    print (' x ' if c > 1 else ' = ', end='')
    c -= 1
print(f)

'''f*=c ( para calcualr sem a biblioteca'''
    
    