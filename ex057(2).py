sexo = str (input (' Informe o seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'mMfF':
    sexo = str(input(' Opção inválida, por favor informe o seu sexo: ')).strip().upper()[0]
print(' Sexo {} registrado!'.format(sexo))