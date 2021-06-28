def contador(i, f, p=1):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    Função criada por Gustavo Guanabara
    """
    for c in range(i, f, p):
        print(c, end=' ')
    print()


contador(2, 10, 2)
contador(1, 10)
