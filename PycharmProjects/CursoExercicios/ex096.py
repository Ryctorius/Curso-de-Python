def area(b, h):
    a = (b * h).__round__(2)
    print(f'A largura do terreno vale {b}m e o comprimento vale {h}m')
    print(f'A Área do terreno é igual a {a}m²')
    linha()


def linha():
    print('-' * 80)


linha()
print(f"{'Boa Tarde! Nesse Programa iremos calcular a área de um terreno':^80}")
linha()
L = float(input('Primeiro digite a Largura do terreno em metros:')).__round__(2)
C = float(input('Agora digite o comprimento do terreno em metros:')).__round__(2)
area(L, C)
