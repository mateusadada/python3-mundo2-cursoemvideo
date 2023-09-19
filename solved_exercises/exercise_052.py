# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

print('Bem-vindo ao programa que verifica se um número é primo!')

numero = int(input('Digite um número natural: '))

if numero < 2:
    print('\n\033[31mInválido! O número precisa ser acima de 1!')
else:
    for i in range(2, numero):
        if numero % i == 0:
            print(f'\n\033[33mO número {numero} não é primo!')
            break
    else:
        print(f'\n\033[32mO número {numero} é primo!')
