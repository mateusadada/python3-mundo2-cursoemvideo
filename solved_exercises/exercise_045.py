# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

print('Bem-vindo ao programa que joga "Jokenpô" com você!')

print('*** JOKENPÔ ***'
      '\n[1] - Pedra'
      '\n[2] - Papel'
      '\n[3] - Tesoura')
usuario = int(input('Escolha uma opção: '))

if usuario != 1 and usuario != 2 and usuario != 3:
    print('\n\033[31mOpção inválida!')
else:
    computador = randint(1, 3)

    print('\n\033[33mPrepara-se para jogar! Em...')
    sleep(1)

    for i in range(3, 0, -1):
        print(i)
        sleep(1)

    if usuario == computador:
        print(f'\n\033[33mEMPATE! Os dois escolheram ', end="")

        if usuario == 1:
            print('PEDRA')
        elif usuario == 2:
            print('PAPEL')
        else:
            print('TESOURA')

    if usuario == 1 and computador == 3 or usuario == 2 and computador == 1 or usuario == 3 and computador == 2:
        print('\n\033[032mVOCÊ GANHOU! ', end='')
        if usuario == 1:
            print('PEDRA vence a/o ', end='')
        elif usuario == 2:
            print('PAPEL vence a/o ', end='')
        else:
            print('TESOURA vence a/o ', end='')

        if computador == 1:
            print('PEDRA')
        elif computador == 2:
            print('PAPEL')
        else:
            print('TESOURA')

    if computador == 1 and usuario == 3 or computador == 2 and usuario == 1 or computador == 3 and usuario == 2:
        print('\n\033[031mVOCÊ PERDEU! ', end='')
        if usuario == 1:
            print('PEDRA perde para a/o ', end='')
        elif usuario == 2:
            print('PAPEL perde para a/o ', end='')
        else:
            print('TESOURA perde para a/o ', end='')

        if computador == 1:
            print('PEDRA')
        elif computador == 2:
            print('PAPEL')
        else:
            print('TESOURA')
