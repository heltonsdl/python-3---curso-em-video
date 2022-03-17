frase = str (input (' Escreva uma frase: ')).strip().upper()
quebra = frase.split()
junto = ''.join(quebra)
inv = ''
for letras in range (len(junto) -1,-1,-1):
    inv+=junto[letras]
if junto == inv:
    print(' É uma frase palíndroma')
else:
    print(' Não é uma frase palíndroma!')
print(' A frase informada foi {} o inverso é {}'.format(junto, inv))