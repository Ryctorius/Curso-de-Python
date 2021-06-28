P = float(input('Digite o primeiro termo da Progressão Aritmética:'))
R = float(input('Digite a razão dessa PA:'))
print('Os dez primeiros termos dessa PA são:')
print(P)
for c in range(1, 10):
    P = P + R
    print(P)
