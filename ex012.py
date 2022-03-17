valor = float(input('Quanto custa o produto? R$'))
avista = valor - (valor *10/100)
parcelado = valor + ( valor *12/100)
#desc = valor - novo

#print ( 'O valor com o desconto de 5% fica de R$ {}.' .format(desc))

print (' O poduto que custava R$ {}, com o desconto de 10% do pagamento avista sai a R$ {} e com o acrescimo de.12% no parcelado fica {}.'.format (valor, avista, parcelado))
'''Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.'''