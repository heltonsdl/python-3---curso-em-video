from time import sleep

''' Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''


coid = coma = comu = 0
print(' ----- Cadastre um pessoa -------- ')
while True:
    nom = str(input(' NOME: '))
    ida = int(input(' Idade: '))
    sex = str(input(' SEXO: ')).strip().upper()[0]
    while True:
        if sex not in 'FM':
            print(' Opção inválida!')
            sex = str(input(' SEXO: ')).strip().upper()[0]
        else:
            break

    per = str(input(' Deseja continuar? ')).strip().upper()[0]
    if ida >= 18:
        coid+= 1
    if sex in 'M':
        coma+= 1
    if sex in 'F' and ida < 20:
        comu+= 1
    if per in 'N':
        break
    while True:
        if per in 'S':
            print(' Novo registro...')
            sleep(1)
            break
        print(' Opção inválida!')
        per = str(input(' Deseja continuar? ')).strip().upper()[0]
        if per in 'S':
            print(' Reiniciando...')
            sleep(1)
            break
        if per in 'N':
            print(' Enccerrando...')
            sleep(1)
            break
    if per in 'N':
        break

print(f'Foram cadastradas {coid} pessoas acima de 18 anos')
print(f' O total de homens é: {coma} ')
print(f' O total de mulheres abaixo dos 20 anos é: {comu}')
print(' ENCERRANDO O PROGRAMA!')
sleep(1)



