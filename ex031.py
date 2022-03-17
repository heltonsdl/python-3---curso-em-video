viagem = float ( input (' Escreva aqui quantos quilômetros será a sua viagem: Km/h'))
if viagem <=200.00:
    print (' Sua viagem irá custar R${}'.format(viagem* 0.50))
else:
    print (' Sua viagem ira custar R${}'.format(viagem *0.45))