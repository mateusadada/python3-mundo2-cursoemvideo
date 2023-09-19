# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

print('Bem-vindo ao programa de cálculo da tabuada de um número qualquer!')

numero = int(input('Digite um número: '))

print(f'\n\033[33m*** TABUADA DO {numero} ***\n')

for i in range(1, 11):
    print(f'{numero} x {i:2} = {numero * i:2}')
