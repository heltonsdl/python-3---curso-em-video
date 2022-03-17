m1 = float (input ( ' Digite a primeira nota :'))
m2 = float ( input ( ' Digite a segunda nota:'))
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