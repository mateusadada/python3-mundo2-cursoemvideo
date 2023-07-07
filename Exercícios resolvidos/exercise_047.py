# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

print('Bem-vindo ao programa que exibe todos os números pares entre 1 e 50!\n\033[33m')

for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=', ')
