A = float(input('Digite o comprimento do primeiro segmento de reta: '))
B = float(input('Digite a medida do segundo segmento de reta: '))
C = float(input('Digite a medida do terceiro segmento de reta: '))
if abs(A-C) < B < A+C:
    if abs(A-B) < C < A+B:
        if abs(B-C) < A < B+C:
            print('As medidas de segmento de retas {}, {}, {}, podem sim formar um triângulo'.format(A, B, C))
else:
    print('As medidas de segmento de retas {}, {}, {}, não podem formar um triângulo'.format(A, B, C))
