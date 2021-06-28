N = int(input('Digite um número:'))
X = 0
for c in range(2, N):
    R = N % c
    if R == 0:
        X = X + 1
if X == 0:
    print('O número digitado é primo!')
else:
    print('O número digitado NÃO é primo!')
