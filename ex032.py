from time import sleep
from datetime import date
print (' Ano bissexto?')
ano = int ( input(' Digite aqui o ano:'))
print('   Processando...')
sleep(2)
print ('-==-' *12)
if ano ==0:
    ano = date.today().year # analisa o ano resgistrado no computador em uso
if ano % 4==0 and ano % 100 !=0 or ano %400 ==0:
    print(' O ano {} é bissexto!'.format(ano))
else:
    print (' O ano {} não é bissexto!'.format(ano))
