def metade(n=0, cond=True):
    r = (n/2)
    return moeda(r) if cond is True else r


def dobro(n=0, cond=True):
    r = 2 * n
    if cond:
        return moeda(r)
    else:
        return r


def aumentar(n=0, t=0, cond=True):
    r = ((100+t)/100) * n
    return moeda(r) if cond is True else r


def diminuir(n=0, t=0, cond=True):
    r = ((100-t)/100) * n
    return moeda(r) if cond is True else r


def moeda(n=0, m='R$'):
    return f'{m}{n:.2f}'.replace('.', ',')
