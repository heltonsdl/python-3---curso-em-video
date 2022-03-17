from time import sleep
print (' Olá! estou monitorando a velocidade dos carros nessa via...')
velocidade = float ( input (' Digite aqui sua velocidade atual: km/h'))
print ('PROCESSANDO...')
sleep(2)
print ('-==-' *12)
if velocidade <=80.00:
    print (' Esta tudo certo, pode continuar!')
else:
    rest = velocidade - 80.00
    if velocidade >=100.00:
        print (' Calma ai cara! quer morrer?')
    print ( ' Você esta acima da velocidade permitida para esse trecho, você foi multado no valor de R$ {:.2f}'.format(rest *7))
