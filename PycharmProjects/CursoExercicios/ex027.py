NOME = str(input('Digite seu nome completo:')).strip()
P = NOME.split()
print('Seu primeiro nome é: {}'.format(P[0]))
U = NOME.rfind(' ')
print('Seu ultimo nome é: {}'.format(NOME[U+1:]))
#Na correção o ultimo nome apareceu com o seguinte codigo
#print('Seu ultimo nome é {}'.format(NOME[len(NOME)-1]))
