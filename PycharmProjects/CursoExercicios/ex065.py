NUM = int(input('Digite um valor inteiro:'))
MAIOR = NUM
MENOR = NUM
SOMA = 0
C = 0
R = "S"
while R == "S":
    if NUM > MAIOR:
        MAIOR = NUM
    elif NUM < MENOR:
        MENOR = NUM
    SOMA += NUM
    C += 1
    R = str(input('Deseja continuar: [S ou N]')).upper().strip()
    if R == "S":
        NUM = int(input('Digite um valor inteiro:'))
    elif R == "N":
        print('Programa Finalizado!')
    else:
        quit('OPÇÃO INVÁLIDA!!!')
print('O maior valor digitado foi {} e o menor valor digitado foi {} e a média foi {:.2f}'.format(MAIOR, MENOR, SOMA/C))
