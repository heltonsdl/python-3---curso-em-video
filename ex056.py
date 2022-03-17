somaidade = 0
mediaidade = 0
nomehomem = ''
idadehomem = 0
totmulher20 = 0
for p in range (1,5):
    
    print('=========== {}° PESSOA ==============='.format(p))
    
    nome = str(input('Escreva o seu nome: '))
    
    idade = int(input('Escreva a sua idade: '))
   
    sexo = str(input(' Sexo: [F/M]: '))
    
    somaidade += idade
    
    mediaidade = somaidade / 4
    
    if p == 1 and sexo in 'Mm':
        
        nomehomem = nome
        
        idadehomem = idade
        
        if sexo in 'mM' and idade > idadehomem:
            
            idadehomem = idade
            
            nomehomem = nome

    if sexo in 'fF' and idade < 20:
        
        totmulher20+= 1
        
        
print (' A idade do homem mais velho é {} e o seu nome é {}'.format(idadehomem, nomehomem))
print(' A media de idade do grupo é de {}.'.format(mediaidade))
print (' O total de mulher com menos de 20 anos é {}.'.format(totmulher20))

    
        
        