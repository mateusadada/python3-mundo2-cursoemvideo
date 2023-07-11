# Faça um programa que calcule a soma entre todos os números ímpares e que são múltiplos de três e que se encontram no
# intervalo de 1 até 500.

print('Bem-vindo ao programa de cálculo da soma de todos os múltiplos de três entre 1 e 500!')

total = 0

for i in range(1, 501, 2):
    if i % 3 == 0:
        total += i

print(f'\n\033[33mTotal: {total}')
