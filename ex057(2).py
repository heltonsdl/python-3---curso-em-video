sexo = str (input (' Informe o seu sexo: [M/F]')).strip().upper()[0]

'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.'''


while sexo not in 'mMfF':
    sexo = str(input(' Opção inválida, por favor informe o seu sexo: ')).strip().upper()[0]
print(' Sexo {} registrado!'.format(sexo))