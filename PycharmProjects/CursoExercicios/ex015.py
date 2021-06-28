DIAS = int(input('Por quantos dias o carro foi alugado?'))
RODA = float(input('Qual a quilometragem percorrida pelo veículo?(Em Km)'))
CUSTO = (60*DIAS)+(0.15*RODA)
print('O preço total a ser pago pelo aluguel do carro é de R$ {:.2f}'.format(CUSTO))
