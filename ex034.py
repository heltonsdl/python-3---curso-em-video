from time import sleep
print (' Seu setor esta recebendo um aumento pelo bom desempenho!')
print ('=' *40)
salário = float (input (' Digite o seu salário para que eu possa calcular pra você: R$'))
print ('PROCESSANDO...')
sleep(2)
if salário >= 1250.00:
    print (' Você recebeu 10% de aumento e seu salário passa a ser R${:.2f}'.format(salário + (salário * 10 /100)))
else:
    print (' Você recebeu 15% de aumento e seu salário passa a ser R${:.2f}'.format(salário + (salário *15 /100)))