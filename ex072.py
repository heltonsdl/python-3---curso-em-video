quest = 'S'

'''Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''



while True:
    while True:
        valor = int (input(f'Escreva um número entre 0 e 20: '))
        if valor < 0 or valor > 20:
            print(f' Tente novamente')
        else:
            break
    cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
            'Treze', 'Quartose', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
    print(f' Você digitou  {cont[valor]}')
    quest = str ( input(f' Deseja continuar? [S/N]')).strip().upper()[0]
            
    while quest not in'SsNn':
        quest = str ( input(f' Deseja continuar? [S/N]')).strip().upper()[0]
    if quest in'Nn':
        break
    
        
