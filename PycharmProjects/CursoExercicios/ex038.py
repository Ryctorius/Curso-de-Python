PRIMEIRO = int(input('Digite um numero inteiro:'))
SEGUNDO = int(input('Digite outro numero inteiro:'))
if PRIMEIRO > SEGUNDO:
    print('O primeiro valor (%i) é maior q o segundo (%i)!' % (PRIMEIRO, SEGUNDO))
elif SEGUNDO > PRIMEIRO:
    print('O segundo número {} é maior q o primeiro {}!'.format(SEGUNDO, PRIMEIRO))
else:
    print('Os números digitados são iguais!')
