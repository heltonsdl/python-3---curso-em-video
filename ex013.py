salário = float(input(' Qual o salário do funcionário? R$'))
aumento = salário + (salário * 15/100)
print (' O salário do funcionário que era de R$ {:.2f}, passa a ser de R${:.2f} com 15% de aumento.'.format(salário, aumento))
