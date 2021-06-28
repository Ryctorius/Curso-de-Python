import datetime
DATA = datetime.datetime.now()
ANO = int(input('Digite o ano de nascimento do atleta:'))
D = DATA.year - ANO
if D <= 9:
    print('Sua categoria é MIRIM!')
elif D <= 14:
    print('Sua categoria é INFANTIL!')
elif D <= 19:
    print('Sua categoria é JUNIOR!')
elif D <= 20:
    print('Sua categoria é SÊNIOR!')
else:
    print('Sua categoria é MASTER!')
