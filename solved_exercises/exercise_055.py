# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

print('Bem-vindo ao programa de cálculo do maior e menor peso de cinco pessoas!')

for i in range(5):
    peso = float(input(f'{i + 1}º peso: '))

    if i == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso

        if peso < menor:
            menor = peso

print(f'\nMaior peso: \033[33m{maior:.1f} kg\033[m'
      f'\nMenor peso: \033[33m{menor:.1f} kg\033[m')
