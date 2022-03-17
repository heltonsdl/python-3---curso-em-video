somaidade = 0
mediaidade = 0
nomehomem = ''
idadehomem = 0
totmulher20 = 0

''' Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''


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

    
        
        