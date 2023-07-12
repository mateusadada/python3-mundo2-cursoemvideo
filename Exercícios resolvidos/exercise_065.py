# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
# valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar
# a digitar valores.

from time import sleep

print('Bem-vindo ao programa de cálculo da média de N números, além do maior e menor valores lidos!', end='')

continuar = ''
total = 0
contador = 0
maior = 0
menor = 0

while continuar != 'N':
    numero = int(input('\nDigite um número inteiro: '))

    contador += 1
    total += numero
    media = total / contador

    # primeira digitação que inclui o maior e o menor
    if contador == 1:
        maior = numero
        menor = numero

    # verificação se maior
    if numero > maior:
        maior = numero

    # verificação se menor
    if numero < menor:
        menor = numero

    print(f'\033[33mForam digitados {contador} número(s) resultando na média {media:.1f}'
          f'\nMaior número: {maior}'
          f'\nMenor número: {menor}\033[m')

    # verificação se deseja continuar no loop
    continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]

print('\n*** Saindo do programa ***')
sleep(1)
print('=' * 26)
print('Programa finalizado! Até logo')
