def metade(n=0, cond=True):
    r = (n/2)
    if cond:
        return moeda(r)
    else:
        return r


def dobro(n=0, cond=True):
    r = 2 * n
    if cond:
        return moeda(r)
    else:
        return r


def aumentar(n=0, t=0, cond=True):
    r = ((100+t)/100) * n
    if cond:
        return moeda(r)
    else:
        return r


def diminuir(n=0, t=0, cond=True):
    r = ((100-t)/100) * n
    if cond:
        return moeda(r)
    else:
        return r


def moeda(n=0, m='R$'):
    return f'{m}{n:.2f}'.replace('.', ',')


def traco():
    print('-'*40)


def resumo(p=0, aum=0, dim=0):
    traco()
    print(f"{'RESUMO DO VALOR':^40}")
    traco()
    print(f"{'Peço Analisado:'}{moeda(p):>25}")
    print(f"{'Metade do preço:'}{metade(p):>24}")
    print(f"{'Dobro do preço:'}{dobro(p):>25}")
    print(f"{aum}{'% de aumento:'} {aumentar(p, aum):>24}")
    print(f"{dim}{'% de redução:'} {aumentar(p, dim):>24}")
    traco()
