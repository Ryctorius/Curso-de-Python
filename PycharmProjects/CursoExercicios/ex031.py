D = float(input('Digite a distância da viagem em Km: '))
if D <= 200:
    P = D*0.5
else:
    P = D*0.45
print('O custo da viagem é de R${:.2f}'.format(P))
