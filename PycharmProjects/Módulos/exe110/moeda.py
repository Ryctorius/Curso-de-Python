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


def resumo(p=0, aum=10, dim=5):
    traco()
    print(f"{'RESUMO DO VALOR':^40}")
    traco()
    print(f"{'Peço Analisado:'}\t\t\t\t\t{moeda(p)}")
    print(f"{'Metade do preço:'}\t\t\t\t{metade(p)}")
    print(f"{'Dobro do preço:'}\t\t\t\t\t{dobro(p)}")
    print(f"{aum}{'% de aumento:'}\t\t\t\t\t{aumentar(p, aum)}")
    print(f"{dim}{'% de redução:'}\t\t\t\t\t{diminuir(p, dim)}")
    traco()
