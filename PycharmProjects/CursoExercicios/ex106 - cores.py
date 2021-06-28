from time import sleep
c = ('\033[m',           # 0-sem cores
    '\033[0;97;41m',     # 1-vermelho
    '\033[0;97;42m',     # 2-verde
    '\033[0;30;43m',     # 3-amarelo
    '\033[0;97;44m',     # 4-azul
    '\033[0;30;45m',     # 5-roxo
    '\033[7;97m'         # 6-branco
    )


def ajuda(txt):
    print(c[6], end='')
    help(txt)
    print(c[0], end='')


def til(frase, cor=0):
    print(c[cor], end='')
    print('~'*(len(frase) + 4))
    print(f'  {frase}')
    print('~' * (len(frase) + 4))
    print(c[0], end='')


while True:
    til('SISTEMA DE AJUDA PyHELP', 2)
    r = str(input('Função ou Biblioteca >')).lower()
    if r == 'fim':
        til('FIM DO PROGRAMA', 1)
        break
    else:
        til(f'Acessando o manual do comando {r}', 4)
        sleep(2)
        ajuda(r)
