PRIM = float(input('Digite o primeiro termo da PA:'))
R = float(input('Digite a razão da PA:'))
NUM = PRIM
if R > 0:
    while NUM < ((10*R) + PRIM):
        print(NUM)
        NUM += R
else:
    while NUM > ((10*R) + PRIM):
        print(NUM)
        NUM += R
print('FIM')
"""No outro exercicio eu fiz com contador até 10, nesse fiz igual ao exemplo do autor no outro exercicio"""
