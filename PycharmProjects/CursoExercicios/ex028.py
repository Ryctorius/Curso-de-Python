import emoji
import random
n = random.randint(0, 5)
a = int(input('Digite um numero inteiro de 0 a 5: '))
if n == a:
    print('Parabéns! Você venceu!!!')
else:
    print('Que pena, você errou! O número sorteado foi {}.'.format(n))
print(emoji.emojize('Obrigado por jogar conosco :sunglasses:'))
