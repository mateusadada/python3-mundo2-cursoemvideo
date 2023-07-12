# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência
# de Fibonacci.
# Exemplo: 0 - 1 - 1 - 2 - 3 - 5 - 8

print('Bem-vindo ao programa de cálculo de uma Sequência de Fibonacci!')

sequencia = int(input('Digite a quantidade de elementos para listar: '))

numero1 = 0
numero2 = 1

contador = 0

print('\n\033[33m0', end=' - ')

while contador < sequencia - 1:
    if contador + 1 == sequencia - 1:
        print(numero2)
    else:
        print(numero2, end=' - ')

    proximo_numero = numero1 + numero2
    numero1 = numero2
    numero2 = proximo_numero

    contador += 1
