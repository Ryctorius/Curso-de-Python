from math import sqrt
ca = float(input('Digite o cateto adjacente:'))
co = float(input('Digite o cateto oposto:'))
hip = sqrt(pow(ca, 2) + pow(co, 2))
print('Sua hipotenusa é igual a: {:.2f}'.format(hip))
