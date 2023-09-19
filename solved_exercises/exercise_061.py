# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura while.

print('Bem-vindo ao programa de cálculo de uma PA!')

primeiro_termo = int(input('Digite o 1º termo de uma PA: '))
razao = int(input('Razão: '))

print()

contador = 0

while contador < 10:
    print(f'{contador + 1}º termo: \033[33m{primeiro_termo + (razao * contador)}\033[m')
    contador += 1
