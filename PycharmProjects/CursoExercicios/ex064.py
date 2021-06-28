NUM = int(input('Digite um número inteiro: OBS.: Para parar o programa digite 999'))
SOMA = C = 0
while NUM != 999:
    SOMA += NUM
    C += 1
    NUM = int(input('Digite um número inteiro: OBS.: Para parar o programa digite 999'))
print('Foram digitados {} números e o somatório deles foi {}'.format(C, SOMA))
