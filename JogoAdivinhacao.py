from random import randint
from time import sleep

print('======== JOGO DA ADVINHAÇÃO ========')
sleep(.5)

while True:
    op = str(input('Gostaria de ver as regras? [S/N]\nDigite: '))

    if op.lower() == 's':
        print('A máquina escolherá um número aleatório de acordo com a dificuldade')
        sleep(.5)
        print('Digite um valor para a dificuldade, e tente adivinhar o número escolhido...')
        sleep(.5)
        break

    elif op.lower() == 'n':
        break

maxn = int(input('\nDigite a dificuldade: '))
num = randint(1, maxn)
sleep(.5)
print(f'A máquina escolheu um número entre 1 e {maxn}, tente adivinhar')
print('-------------------------------------')
sleep(.5)
count = 1

while True:
    tent = int(input('Digite um valor: '))

    if tent > num:
        print('Muito Alto')
    elif tent < num:
        print('Muito Baixo')
    elif tent == num:
        break

    count += 1

print()
print('{:=^25}'.format(' PARABÉNS '))
print('Você venceu!!!')
print(f'\nNúmero de Tentativas: {count}')

if count == 1:
    print('''╔═══════════════════════════╗
║ NA PRIMEIRA TENTATIVA !!! ║
╚═══════════════════════════╝''')
