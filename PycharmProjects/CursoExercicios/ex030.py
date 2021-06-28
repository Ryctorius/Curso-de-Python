N = int(input('Digite um valor inteiro diferente de zero:'))
if N == 0:
    print('Eu falei diferente de 0 seu doente!')
else:
    if (N % 2) == 1:
        print('O número {} é impar'.format(N))
    else:
        print('O número {} é par'.format(N))
