N = int(input('Digite um número de 0 a 9999:'))
u = N//1 % 10
d = N//10 % 10
c = N//100 % 10
m = N//1000 % 10
print('Unidade:{}'.format(u))
print('Dezena: {}'.format(d))
print('Centena:{}'.format(c))
print('Milhar:{}'.format(m))
