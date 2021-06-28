SOMA = CONT = 0
while True:
    N = int(input('Digite um número inteiro (999 para parar):'))
    if N == 999:
        break
    SOMA += N
    CONT += 1
print(f'A quantidade de números digitados foi {CONT} e o somatório deles é igual a {SOMA}')
