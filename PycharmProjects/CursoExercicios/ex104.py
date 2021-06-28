def leiaint(frase):
    while True:
        num = str(input(frase))
        if num.isnumeric():
            num = int(num)
            if type(num) == int:
                return num
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido\033[m')


n = leiaint('Digite um número inteiro:')
print(f'Você acabou de digitar o número {n}')
