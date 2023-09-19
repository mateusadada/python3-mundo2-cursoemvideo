# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar
# ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

from time import sleep

total_gasto = produto_maior_1000 = nome_produto_mais_barato = 0
preco_produto_mais_barato = -1

print('Bem-vindo ao programa de cálculo a partir do preço de N produtos!', end='')

while True:
    nome = str(input('\nDigite o nome do produto: ')).strip()
    preco = float(input('Preço: R$ '))

    # validação se quer continuar no programa
    while True:
        continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]

        if continuar not in 'SN':
            print('\033[31mEntrada inválida! Tente novamente.\033[m')
        else:
            break

    # inclusão dos critérios
    total_gasto += preco

    if preco > 1000:
        produto_maior_1000 += 1

    if preco_produto_mais_barato == -1:
        preco_produto_mais_barato = preco
        nome_produto_mais_barato = nome

    if preco < preco_produto_mais_barato:
        preco_produto_mais_barato = preco
        nome_produto_mais_barato = nome

    # saída do programa
    if continuar == 'N':
        print(f'\n\033[33mTotal gasto na compra: R$ {total_gasto:.2f} reais'
              f'\n{produto_maior_1000} produto(s) custam mais de R$ 1.000,00 reais'
              f'\nO produto mais barato é a/o {nome_produto_mais_barato} custando R$ {preco_produto_mais_barato:.2f}'
              f' reais\033[m')

        print('\nSaindo do programa...')
        sleep(2)
        print('Programa finalizado. Obrigado por utilizar. Até logo!')
        break
