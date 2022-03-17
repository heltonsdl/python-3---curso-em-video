from datetime import date

'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

Aula Anterior
Voltar para Módulo
Próximo'''



atual = date.today().year
totmaior = 0
totmenor = 0
for c in range (1, 8):
    ano = int (input(' Escreva o ano de nascimento da {}° pessoa: '.format(c)))
    if atual - ano <=21:
        totmenor+=1
    else:
        totmaior+=1
print(' O total de pessoas maiores de idade é {}'.format(totmaior))
print(' E o total de pessoas menores de idade é {}.'.format(totmenor))
        
    