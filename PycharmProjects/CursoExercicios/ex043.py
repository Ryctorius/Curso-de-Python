from math import pow
PESO = float(input('Digite seu peso em Kg:'))
ALTURA = float(input('Digite sua altura em metros:'))
IMC = PESO/pow(ALTURA, 2)
if IMC < 18.5:
    print('Seu IMC é {:.2f}ABAIXO DO PESO!'.format(IMC))
elif IMC < 25:
    print('Seu IMC é %.2f PESO IDEAL!' % IMC)
elif IMC < 30:
    print('Seu IMC é {:.2f} SOBREPESO!'.format(IMC))
elif IMC < 40:
    print('Seu IMC é %.2f OBESIDADE!' % IMC)
else:
    print('Seu IMC é {:.2f} OBESIDADE MÓRBIDA!'.format(IMC))
