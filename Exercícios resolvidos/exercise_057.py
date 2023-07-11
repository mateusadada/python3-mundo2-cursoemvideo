# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a
# digitação novamente até ter um valor correto.

print('Bem-vindo ao programa que permite apenas entradas de "M" ou "F"!')

sexo = str(input('Digite o sexo (M ou F): ')).strip().upper()

while sexo not in 'MmFf':
    print('\033[31mEntrada inválida! Tente novamente...\033[m\n')
    sexo = str(input('Digite o sexo (M ou F): ')).strip().upper()

print(f'\n\033[33mO sexo digitado foi {sexo}')
