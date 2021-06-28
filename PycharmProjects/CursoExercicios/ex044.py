CUSTO = float(input('Digite o valor do produto em reais: R$'))
print('Escolha a opção da forma de pagamento:')
print('Digite [0] para pagamento à vista dinheiro/cheque')
print('Digite [1] para pagamento à vista no cartão')
print('Digite [2] para pagamento parcelado em 2x no cartão')
print('Digite [3] para pagamento parcelado em 3x ou mais no cartão')
FORMA = int(input())
if FORMA == 0:
    print('A opção selecionada foi pagamento à vista dinheiro/cheque o valor a ser pago será R$%.2f' % (CUSTO*0.9))
elif FORMA == 1:
    print('A opção selecionada foi pagamento à vista no cartão o valor a ser pago será R${:.2f}'.format(CUSTO*0.95))
elif FORMA == 2:
    print('A opção selecionada foi pagamento parcelado em 2 vezes de R${:.2f}'.format(CUSTO/2))
elif FORMA == 3:
    N = int(input('A opção selecionada foi pagamento parcelado, digite o número de parcelas desejado:'))
    print('A opção selecionada foi pagamento parcelado em {} vezes de R${:.2f}'.format(N, (1.2*CUSTO/N)))
else:
    print('Opção de pagamento inválida!')
