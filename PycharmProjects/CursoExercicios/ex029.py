V = float(input('Digite qual a velocidade do carro em Km/h : '))
if V > 80:
    VALOR = 7*(V-80)
    print('Você foi multado e o valor a ser pago é de R$ {:.2f} '.format(VALOR))
