def leiaint(frase):
    while True:
        try:
            num = int(input(frase))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('O usuário preferiu não digitar nada')
            return 0
        else:
            return num


def leiafloat(frase):
    while True:
        try:
            num = float(input(frase))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número real válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('O usuário preferiu não digitar nada')
            return 0
        else:
            return num


n = leiaint('Digite um número inteiro:')
m = leiafloat('Digite um número real:')
print(f'O número inteiro digitado foi {n} e o numero real digitado foi {m}')
