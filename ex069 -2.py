print (' ----- CADASTRE UMA PESSOA ------ ')
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
    