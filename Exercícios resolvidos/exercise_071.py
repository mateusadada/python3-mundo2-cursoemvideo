# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor
# a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# Observação: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

from time import sleep

print('Bem-vindo ao programa de simulação do funcionamento de um caixa eletrônico!', end='')

while True:
    while True:
        valor = int(input('\nDigite o valor a ser sacado: R$ '))

        if not valor > 0:
            print('\033[31mEntrada inválida! Informe um valor positivo.\033[m', end='')
        else:
            break

    valor_reduzido = valor

    print('\n\033[32m*** CÉLULAS PARA RECEBER ***\033[33m')

    # cálculos das quantidades de células
    if valor_reduzido // 50 > 0:
        print(f'{valor_reduzido // 50} célula(s) de R$ 50,00 reais')

    valor_reduzido %= 50

    if valor_reduzido // 20 > 0:
        print(f'{valor_reduzido // 20} célula(s) de R$ 20,00 reais')

    valor_reduzido %= 20

    if valor_reduzido // 10 > 0:
        print(f'{valor_reduzido // 10} célula(s) de R$ 10,00 reais')

    valor_reduzido %= 10

    if valor_reduzido // 1 > 0:
        print(f'{valor_reduzido // 1} célula(s) de R$ 1,00 reais')

    # validação se quer continuar no programa
    while True:
        continuar = str(input('\n\033[mDeseja continuar [S/N]? ')).strip().upper()[0]

        if continuar not in 'SN':
            print('\033[31mEntrada inválida! Informe "sim" ou "não".\033[m', end='')
        else:
            break

    # saída do programa
    if continuar == 'N':
        print('\nSaindo do programa...')
        sleep(2)
        print('Programa finalizado. Obrigado por utilizar. Até logo!')
        break
