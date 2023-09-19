# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
# se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

from time import sleep

pessoa_maior_18 = homem = mulher_menos_20 = 0

print('Bem-vindo ao programa de cálculo a partir da idade e do sexo de N pessoas!', end='')

while True:
    idade = int(input('\nDigite a idade: '))

    # validação do sexo
    while True:
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]

        if sexo not in 'MF':
            print('\033[31mEntrada inválida! Tente novamente.\033[m')
        else:
            break

    # inclusão dos três critérios
    if idade > 18:
        pessoa_maior_18 += 1

    if sexo == 'M':
        homem += 1

    if sexo == 'F' and idade < 20:
        mulher_menos_20 += 1

    # validação da continuação do programa
    continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]

    if continuar == 'N':
        # exibição do resultado
        print(f'\nPessoas que têm mais de 18 anos: {pessoa_maior_18}'
              f'\nHomens que foram cadastrados: {homem}'
              f'\nMulheres que tem menos de 20 anos: {mulher_menos_20}')

        print('\n\033[33mSaindo do programa...')
        sleep(2)
        print('Programa finalizado. Obrigado por utilizar. Até logo!')
        break
