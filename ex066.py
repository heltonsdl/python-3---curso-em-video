cont = soma = n = 0

while True:
    n = int(input(' Digite um número (999 para parar) : '))


    if n == 999:
        break
    soma += n
    cont += 1


print(f' Foram digitados {cont} e a soma deles é {soma}')
