from datetime import datetime


def voto(n):
    if n < 16:
        return 'NÃO VOTA!'
    elif n < 18 or n > 65:
        return 'VOTO OPCIONAL'
    else:
        return 'VOTO OBRIGATÓRIO'


nasc = int(input('Digite seu ano de nascimento:'))
num = datetime.now().year - nasc
print(f'Com {num} anos: {voto(num)}')
