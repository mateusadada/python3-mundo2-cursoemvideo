# Escreva um programa que leia dois números inteiros e compare-os. Mostrando uma mensagem na tela:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

print('Bem-vindo ao programa que compara dois números inteiros!')

numero1 = int(input('1º número: '))
numero2 = int(input('2º número: '))

if numero1 > numero2:
    print(f'\nO primeiro valor \033[33m({numero1})\033[m é maior')
elif numero2 > numero1:
    print(f'\nO segundo valor \033[33m({numero2})\033[m é maior')
else:
    print(f'\nNão existe valor maior, os dois são iguais \033[33m({numero1})\033[m')
