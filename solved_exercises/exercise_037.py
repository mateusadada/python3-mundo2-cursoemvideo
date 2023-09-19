# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de
# conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

print('Bem-vindo ao programa de cálculo de conversão de binário, octal e hexadecimal!')

numero = int(input('Digite um número inteiro: '))

print('\n*** CONVERSÕES ***'
      '\n[1] - Binário'
      '\n[2] - Octal'
      '\n[3] - Hexadecimal')
opcao = int(input('Escolha uma opção acima: '))

if opcao == 1:
    print(f'\n\033[33m{numero} em binário é {bin(numero)[2:]}')
elif opcao == 2:
    print(f'\n\033[33m{numero} em octal é {oct(numero)[2:]}')
elif opcao == 3:
    print(f'\n\033[33m{numero} em hexadecimal é {hex(numero)[2:]}')
else:
    print('\n\033[031mOpção inválida!')
