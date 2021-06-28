N = int(input('Digite quantos termos da sequencia de Fibonacci você deseja:'))
SEQ1 = 1
SEQ2 = 1
DEV = 1
print("0->1", end="")
while N-2 > 0:
    print("->{}".format(SEQ1), end="")
    DEV = SEQ1
    SEQ1 += SEQ2
    SEQ2 = DEV
    N -= 1
