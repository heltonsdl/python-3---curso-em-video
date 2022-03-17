print (' ----- CADASTRE UMA PESSOA ------ ')

'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''

while True:
    nom = str(input(' Nome: '))
    ida = int(input(' Idade: '))
    sex = str(input(' Sexo: ')).strip().upper()[0]
    ctn = str(input(' Deseja continuar? ')).strip().upper()[0]
    print('==' *12)
    if ctn in 'N':
        break
    if ctn not in 'NS':
        while True:
            print (' Opção inválida!')
            ctn = str(input(' Deseja continuar?')).strip().upper()[0]
            print('==' *12)
            if ctn in 'N':
                print(' Finalizando...')
                break
    
            
            
    
print (' Acabou!')
    