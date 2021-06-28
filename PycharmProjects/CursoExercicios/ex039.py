from datetime import date
DATA = date.today().year
ANO = int(input('Digite seu ano de nascimento:'))
D = DATA - ANO
if D == 18:
    print('Chegou a sua hora!! Aliste-se esse ano!')
elif D > 18:
    print('Já passou da hora! Você deveria ter se alistado há {} anos atrás. Regularize o quanto antes!!'.format(D-18))
else:
    print('Ainda não chegou a sua hora! Faltam {} anos para chegar a sua vez'.format(18-D))
