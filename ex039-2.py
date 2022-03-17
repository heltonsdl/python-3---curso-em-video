from datetime import date
print (' Confira a data do alistamento militar:')
nasc = int (input (' Digite a sua data de nascimento:'))
atual = date.today().year
idade = atual - nasc
if idade >18:
    saldo = idade - 18
    ano = atual - saldo
    print (' Sua idade é {} se passou {} anos do alistamento que foi em {}.'.format(idade, saldo, ano))

elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print (' Sua idade é {} faltam {} anos para o alistamento, que será em {}.'.format(idade, saldo, ano))
else:
    print(' Seu alistamento é esse ano!.')