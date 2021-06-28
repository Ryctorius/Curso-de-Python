VAL = list()
for c in range(0, 5):
    n = int(input('Digite um valor:'))
    if c == 0 or n > VAL[-1]:
        VAL.append(n)
    else:
        pos = 0
        while pos < len(VAL):
            if n <= VAL[pos]:
                VAL.insert(pos, n)
                break
            pos += 1
print(f'Os valores digitados em ordem foram {VAL}')
