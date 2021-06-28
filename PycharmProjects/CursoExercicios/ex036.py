CASA = float(input('Digite o valor da casa em reais:R$'))
SALARIO = float(input('Digite o valor do seu salário em reais:R$'))
TEMPO = int(input('Agora digite em quanto tempo o senhor deseja pagar a casa:'))
PRESTACAO = CASA / (TEMPO*12)
if PRESTACAO > (0.3*SALARIO):
    print('O valor da prestação mensal seria de R${:.2f}.Empréstimo não autorizado!'.format(PRESTACAO))
else:
    print('Empréstimo autorizado com o valor mensal de R${:.2f} que deverá ser pago em {}anos'.format(PRESTACAO, TEMPO))
