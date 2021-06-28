N = int(input('Digite um numero para calcularmos o fatorial:'))
FAT = N
NUM = N
print(N, end="")
N -= 1
while N > 0:
    print("*{}".format(N), end="")
    FAT *= N
    N -= 1
print("!")
print('O fatorial de {} é igual a {}.'.format(NUM, FAT))
