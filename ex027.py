nm = str(input('\033[31mEscreva seu nome completo: \033[m'))
pr = nm.split()

#cores = { 'limpa' : '\033[m', 'azul' : '\033[34m', 'vermelho' : '\033[31m', ' amarelo' : '\033[33m'}

 

print (' Seu primeiro nome é {}.' .format( pr[0]))
print (' E seu último nome é {}.' .format( pr[len (pr )-1]))