def notas(*num, sit=False):
    maior = menor = soma = 0
    di = dict()
    for c in range(0, len(num)):
        if c == 0:
            maior = num[0]
            menor = num[0]
        elif num[c] > maior:
            maior = num[c]
        elif num[c] < menor:
            menor = num[c]
        soma += num[c]
    media = (soma/len(num)).__round__(2)
    di['total'] = len(num)
    di['maior'] = maior
    di['menor'] = menor
    di['media'] = media
    if sit:
        if media >= 7:
            di[situação] = 'BOA'
        elif media >= 5:
            di['situação'] = 'RAZOÁVEL'
        else:
            di['situação'] = 'RUIM'
    return di


resp = notas(5.5, 10, 2.5, 6.5, sit=True)
print(resp)
