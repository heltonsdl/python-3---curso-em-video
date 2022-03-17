from datetime import date
print ('\033[1;32m Vamos verificar sobre o alistamento militar!\033[m')
print ('\033[1;33m-==- \033[m' *10)
data = int ( input ('Escreva o ano do seu nascimento:'))
atual = date.today().year
idade = (data - atual) * -1
if idade > 18:
    saldo = idade - 18
    print (' Você tem {} anos e ja passou {} anos de se alistar.'.format (idade, saldo))
    print (' Ano de alistamento {}.').format(saldo)
elif idade < 18:
    saldo = 18 - idade
    print (' Você tem {} anos faltam {} anos para o alistamento.'.format(idade, saldo))

elif idade == 18 :
    print (' Você ja tem {} Esta na hora!'.format(idade))