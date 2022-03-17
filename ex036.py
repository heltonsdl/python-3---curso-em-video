casa = float (input (' Digite o valor da casa: R$'))
salário = float (input (' Digite o valor do seu salário:R$'))
anos = int (input (' Digite em quantos anos quer pagar:'))
limite = salário *30/100
parcela = casa / ( anos *12)


''' Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''



if parcela <= limite:
    print (' Financiamento aprovado!')    
    print (' A casa no valor de R${:.2f}, tera {:.0f} parcelas de R${:.2f}.'.format(casa,(casa /parcela), parcela))
else:
    print (' Financiamento negado!')
    print (' Devido o valor da parcela (R$ {:.2f}) exceder 30% do seu salário, não será possível darmos continuidade.'.format (parcela))