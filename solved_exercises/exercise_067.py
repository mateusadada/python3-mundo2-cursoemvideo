# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O
# programa será interrompido quando o número solicitado for negativo.

from time import sleep

print('Bem-vindo ao programa de cálculo da tabuada de N números!', end='')

while True:
    numero = int(input('\nDigite um número para mostrar a tabuada (negativo para sair): '))

    if numero < 0:
        print('\n\033[33mSaindo do programa...')
        sleep(2)
        print('Programa finalizado. Obrigado por utilizar. Até logo!')
        break

    else:
        print(f'\n*** TABUADA DO NÚMERO {numero} ***')
        for i in range(1, 11):
            print(f'{numero} x {i:2} = \033[33m{numero * i}\033[m')
