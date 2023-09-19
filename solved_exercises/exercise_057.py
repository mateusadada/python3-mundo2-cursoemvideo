# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a
# digitação novamente até ter um valor correto.

print('Bem-vindo ao programa que permite apenas entradas de "M" ou "F"!')

sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]

while sexo not in 'MF':
    sexo = str(input('\033[31mEntrada inválida! Tente novamente...\033[m'
                     '\n\nDigite o sexo (M ou F): ')).strip().upper()[0]

print(f'\n\033[33mO sexo digitado foi {sexo}')
