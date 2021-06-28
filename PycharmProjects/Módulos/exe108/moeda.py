def metade(n=0):
    n = (n/2)
    return n


def dobro(n=0):
    n = 2 * n
    return n


def aumentar(n=0, t=0):
    n = ((100+t)/100) * n
    return n


def diminuir(n=0, t=0):
    n = ((100-t)/100) * n
    return n


def moeda(n=0, m='R$'):
    return f'{m}{n:.2f}'.replace('.', ',')
