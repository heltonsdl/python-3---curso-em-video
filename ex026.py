f = str ( input( 'Escreva alguma frase:'))
print (' Sua frase contém {} letras "as".'.format(f.count('a')))
print (' Ela aparece pela primeira fez na posição {}.'.format(f.find('a')))
print (' E.aparece pela última vez na posição {}.' .format( f.rfind ('a')))
