# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import choice
from time import sleep

print('Bem-vindo ao programa que joga contra o computador na adivinhação de ímpar ou par!', end='')

total_vitorias = 0

while True:
    computador = str(choice(['PAR', 'ÍMPAR']))
    jogador = str(input('\nEscolha PAR ou ÍMPAR: ')).strip().upper()

    if jogador == 'IMPAR':
        jogador = 'ÍMPAR'

    if jogador in 'PARÍMPAR':
        if jogador == computador:
            print(f'\033[32mParabéns! Você acertou. Um ponto para você :)\033[m')
            total_vitorias += 1

        else:
            print(f'\033[33mVocê perdeu! O computador havia escolhido {computador}'
                  f'\nVocê fez {total_vitorias} ponto(s)')

            print('\n\033[33mSaindo do programa...')
            sleep(2)
            print('Programa finalizado. Obrigado por utilizar. Até logo!')
            break

    else:
        print('\033[31mEntrada inválida! Por favor, tente novamente.\033[m')
