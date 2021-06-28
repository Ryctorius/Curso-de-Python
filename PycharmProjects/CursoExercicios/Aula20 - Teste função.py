def continuar(resp):
    while True:
        if resp not in 'NnSs':
            print('Resposta incorreta! Tente novamente.')
            resp = str(input('Deseja continuar?')).strip()[0]
        else:
            break


while True:
    N = str(input('Digite um nome:'))
    r = str(input('Deseja continuar?')).strip()[0]
    continuar(r)
    if r in 'Nn':
        break
