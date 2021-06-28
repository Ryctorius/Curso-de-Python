NOTA1 = float(input('Digite sua primeira nota:'))
NOTA2 = float(input('Digite sua segunda nota:'))
MEDIA = (NOTA1 + NOTA2)/2
if MEDIA >= 7:
    print('Parabéns! Sua nota foi {:.2f} , você está APROVADO!!!'.format(MEDIA))
elif MEDIA < 5:
    print('Não foi dessa vez. Sua nota foi {:.2f} portanto você esta REPROVADO!'.format(MEDIA))
else:
    print('Sua nota foi {:.2f}, com isso você está de RECUPERAÇÃO!'.format(MEDIA))
