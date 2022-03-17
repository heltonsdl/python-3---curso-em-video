m1 = float (input ( ' Digite a primeira nota :'))
m2 = float ( input ( ' Digite a segunda nota:'))


'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO'''


media = (m1 + m2)/2
print ('='*40)
print (' Tirando {} e {} a medida do aluno é {}.'.format(m1, m2, media))
print ('=' *40)
if media < 5.00:
    print (' \033[1;31mSua média foi {} você foi Reprovado!\033[m'.format (media))
elif media >= 5 and media <=6.9:
    print ('\033[1;33m Sua média foi {} você está de Recuperação!\033[m'.format(media))
elif media >= 7:
    print (' \033[1;34mAprovado!\033[m')