# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
# sendo a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas
# (desconsiderando o flag).

from time import sleep

print('Bem-vindo ao programa de cálculo da soma de N números!')

contador = total = 0

while True:
    numero = int(input('Digite um número (999 p/ sair): '))

    if numero == 999:
        print(f'\n\033[33mForam digitados {contador} número(s) totalizando a soma de {total}')

        print('\n\033[33mSaindo do programa...')
        sleep(2)
        print('Programa finalizado. Obrigado por utilizar. Até logo!')
        break
    else:
        contador += 1
        total += numero
