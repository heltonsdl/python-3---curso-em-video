print(' ------ Loja amigão ---------')

'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''

totp = tot1k = cont = menor = 0
barato = ' '
while True:
    pro = str(input(' Produto: '))
    pre = float(input(' Preço: R$'))
    cont+= 1
    if cont == 1 or pre < menor:
        menor = pre
        barato = pro
 
    tp = ' '
    totp = totp + pre
    if pre > 1000:
        tot1k+= 1
    while tp not in 'NS':
        tp = str(input(' Deseja continuar? ')).strip().upper()[0]
        print('*"'*24)
    if tp == 'N':
        break
print(' Acabou ')
print(f' O valor total da compra foi de R${totp}')
print(f' O total de produtos acima de R$1000,00 é: {tot1k}')
print(f'O produto mais barato foi {pro} que custa R${menor}')
