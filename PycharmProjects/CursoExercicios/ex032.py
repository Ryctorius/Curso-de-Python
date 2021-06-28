from datetime import date
ANO = int(input('Digite um ano: \n Obs.: Digite 0 caso queira saber do ano atual   '))
if ANO == 0:
    ANO = date.today().year
if ANO % 4 == 0 and ANO % 100 != 0 or ANO % 400 == 0:
    print('O ano {} é bissexto!'.format(ANO))
else:
    print('O ano {} não é um ano bissexto!'.format(ANO))
