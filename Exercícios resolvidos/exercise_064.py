# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
# valor 999, sendo a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando o flag).

print('Bem-vindo ao programa de cálculo da soma de N números!')

numero = 0
total = 0
contador = 0

while numero != 999:
    numero = int(input('Digite um número inteiro (999 p/ sair): '))

    if numero != 999:
        contador += 1
        total += numero

print(f'\n\033[33mForam digitados {contador} número(s) resultando na soma de {total}')
