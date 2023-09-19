# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria, conforme a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

from datetime import date

print('Bem-vindo ao programa de cálculo da categoria de um atleta!')

ano_de_nascimento = int(input('Informe o ano de nascimento: '))

idade = date.today().year - ano_de_nascimento

print(f'\nIdade: \033[33m{idade}\033[m'
      f'\nCategoria: \033[33m', end='')

if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JÚNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')
