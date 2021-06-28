S = float(input('Digite o salario do funcionario em reais: '))
if S > 1250:
    S = S*1.1
else:
    S = S*1.15
print('Seu novo salario com aumento será: R$ {:.2f}'.format(S))
