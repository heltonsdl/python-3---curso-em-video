from datetime import date
print (' Vamos definir em qual categoria de natação você se enquadra:')
ano = int (input (' Digite o ano do seu nascimento:'))
atual = date.today().year
idade = (ano - atual) * -1
if idade > 20:
    print (' Categoria MASTER')
elif idade <=9:
    print (' Categoria MIRIM')
elif idade > 9 and idade <=14:
    print (' Categoria infantil')
elif idade > 14 and idade <=19:
    print (' Categoria junior')
elif idade == 20:
    print ('Sênior')    
