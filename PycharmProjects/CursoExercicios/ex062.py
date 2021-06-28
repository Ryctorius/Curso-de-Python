NUM = float(input('Digite o primeiro termo da PA:'))
R = float(input('Digite a razão da PA:'))
CONT = 0
while CONT < 10:
    print(NUM)
    NUM += R
    CONT += 1
PLUS = int(input('Digite mais quantos termos você quer ver: (obs.: 0 para finalizar)'))
while PLUS != 0:
    while PLUS != 0:
        print(NUM)
        NUM += R
        PLUS -= 1
        CONT += 1
    PLUS = int(input('Digite mais quantos termos você quer ver: (obs.: 0 para finalizar)'))
print('Programa finalizado exibindo {} termos da PA'.format(CONT))
