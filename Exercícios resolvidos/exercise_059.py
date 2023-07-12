# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

print('Bem-vindo ao programa com um MENU com várias opções de cálculos entre dois valores!')

numero1 = int(input('1º valor: '))
numero2 = int(input('2º valor: '))
opcao = 0

while opcao != 5:
    opcao = int(input('\n*** ESCOLHA UMA OPERAÇÃO ***'
                      '\n[1] Somar'
                      '\n[2] Multiplicar'
                      '\n[3] Maior'
                      '\n[4] Novos números'
                      '\n[5] Sair do programa'
                      '\nOpção: '))

    if opcao == 1:
        print(f'\033[33mA soma dos números {numero1} e {numero2} é {numero1 + numero2}\033[m')

    elif opcao == 2:
        print(f'\033[33mA multiplicação dos números {numero1} e {numero2} é {numero1 * numero2}\033[m')

    elif opcao == 3:
        if numero1 > numero2:
            print(f'\033[33mO número {numero1} é maior que o número {numero2}\033[m')
        elif numero2 > numero1:
            print(f'\033[33mO número {numero2} é maior que o número {numero1}\033[m')
        else:
            print(f'\033[33mOs dois números ({numero1}) são iguais\033[m')

    elif opcao == 4:
        print('\n\033[33mAlterando os dois números...\033[m')
        numero1 = int(input('\033[33m1º valor: \033[m'))
        numero2 = int(input('\033[33m2º valor: \033[m'))

    elif opcao == 5:
        print('\n\033[32mSaindo do programa! Até logo...\033[m')

    else:
        print('\033[31mEntrada inválida! Tente novamente.\033[m')
