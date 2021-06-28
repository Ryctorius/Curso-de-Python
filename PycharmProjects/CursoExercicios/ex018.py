import math
a = float(input('Digite o valor do ângulo em graus:'))
SEN = math.sin(math.radians(a))
COS = math.cos(math.radians(a))
TAN = math.tan(math.radians(a))
print('Para o ângulo {:.2f} º , temos: \n sen= {:.2f} \n cos= {:.2f} \n tan= {:.2f}'.format(a, SEN, COS, TAN))
