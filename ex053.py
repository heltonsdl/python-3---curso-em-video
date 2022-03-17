frase = str (input (' Escreva uma frase: ')).strip().upper()
quebra = frase.split()
junto = ''.join(quebra)
inv = ''

'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.'''


for letras in range (len(junto) -1,-1,-1):
    inv+=junto[letras]
if junto == inv:
    print(' É uma frase palíndroma')
else:
    print(' Não é uma frase palíndroma!')
print(' A frase informada foi {} o inverso é {}'.format(junto, inv))