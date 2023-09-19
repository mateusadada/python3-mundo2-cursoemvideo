# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a
# maioridade e quantas já são maiores (>= 18).

from datetime import date

print('Bem-vindo ao programa de cálculo de maioridade (>= 18) de sete pessoas!')

total_maioridade = total_minoridade = 0

for i in range(7):
    ano_de_nascimento = int(input(f'{i + 1}º pessoa: '))
    idade = int(date.today().year - ano_de_nascimento)

    if idade >= 18:
        total_maioridade += 1
    else:
        total_minoridade += 1

print(f'\n\033[33mMaioridade: {total_maioridade}'
      f'\nMinoridade: {total_minoridade}')
