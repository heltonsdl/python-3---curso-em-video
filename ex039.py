from datetime import date


''' Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

Aula Anterior'''



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