def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    para = n
    while para > 0:
        f *= para
        para -= 1
    if not show:
        return f
    else:
        print(n, end=' ')
        n -= 1
        while n > 0:
            print(f'x {n}', end=' ')
            n -= 1
        print('=', end=' ')
        return f


numero = int(input('Digite um numero:'))
print(fatorial(numero, show=False))
print(fatorial.__doc__)
