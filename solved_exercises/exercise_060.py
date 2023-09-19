# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

print('Bem-vindo ao programa de cálculo de fatorial!')

numero = 0

while numero < 1:
    numero = int(input('Digite um número qualquer positivo: '))

    if numero < 1:
        print('\033[31mEntrada inválida! Tente novamente.\033[m\n')

total = 1

print(f'\n\033[33mFatorial de {numero}! = ', end='')

while numero > 0:
    total *= numero

    if numero == 1:
        print(numero, end=' = ')
    else:
        print(numero, end=' x ')

    numero -= 1

print(total)
