# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
# digitado for ímpar, desconsidere-o.

print('Bem-vindo ao programa de cálculo da soma de seis números pares!')

soma_pares = 0

for i in range(6):
    numero = int(input(f'{i + 1}º número: '))

    if numero % 2 == 0:
        soma_pares += numero

print(f'\n\033[33mSoma dos números pares: {soma_pares}')
