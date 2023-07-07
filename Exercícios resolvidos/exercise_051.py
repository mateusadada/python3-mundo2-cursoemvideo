# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa
# progressão.

print('Bem-vindo ao programa de cálculo de uma PA!')

primeiro_termo = int(input('Digite o 1º termo de uma PA: '))
razao = int(input('Razão: '))

print()

for i in range(10):
    print(f'{i + 1}º termo: \33[33m{primeiro_termo + (razao * i)}\33[m')
