A = float(input('Digite o comprimento do primeiro segmento de reta: '))
B = float(input('Digite a medida do segundo segmento de reta: '))
C = float(input('Digite a medida do terceiro segmento de reta: '))
if B < A+C and C < A+B and A < B+C:
    print('As medidas de segmento de retas {}, {}, {}, podem sim formar um triângulo'.format(A, B, C))
    if A == B == C:
        print('O triêngulo formado será EQUILÁTERO! (todos os lados são iguais)')
    elif A == B or A == C or B == C:
         print('O triangulo formado será ISÓSCELES! (Dois lados iguais e um diferente)')
    else:
         print('O triângulo formado será ESCALENO! (Todos os lados são diferentes)')
else:
    print('As medidas de segmento de retas {}, {}, {}, não podem formar um triângulo'.format(A, B, C))
