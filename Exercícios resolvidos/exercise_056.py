# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do
# grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

print('Bem-vindo ao programa de cálculo da média de idade de um grupo de 4 pessoas!', end='')

total_idade = 0
flag = 0
idade_mulher_menos_20 = 0
maior_idade_homem = None
nome_mais_velho_homem = None

for i in range(4):
    nome = str(input(f'\nNome da {i + 1}º pessoa: '))
    idade = int(input('Idade: '))
    sexo = int(input('Sexo (1-F / 2-M): '))

    total_idade += idade

    if sexo == 2:
        if flag == 0:
            flag = 1
            maior_idade_homem = idade
            nome_mais_velho_homem = nome

        if idade > maior_idade_homem:
            maior_idade_homem = idade
            nome_mais_velho_homem = nome

    elif sexo == 1:
        if idade < 20:
            idade_mulher_menos_20 += 1

media_idade = total_idade / 4

print(f'\n\033[33mA média de idade do grupo é {media_idade:.0f} anos'
      f'\nNome do homem mais velho: {nome_mais_velho_homem}'
      f'\n{idade_mulher_menos_20} mulher(es) têm menos de 20 anos')
