# Faça um programa que leia o ano de nascimento de um jovem e informe, conforme a sua idade, se ele ainda vai se
# alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa
# também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

print('Bem-vindo ao programa de cálculo para o alistamento militar!')

ano_de_nascimento = int(input('Informe o ano de nascimento: '))

idade = date.today().year - ano_de_nascimento

if idade < 18:
    print(f'\n\033[32mVocê ainda vai se alistar no serviço militar!'
          f'\nFalta(m) {18 - idade} ano(s); em {18 - idade + date.today().year}')
elif idade == 18:
    print(f'\n\033[33mVocê está no ano de se alistar no serviço militar (18 anos)!')
else:
    print(f'\n\033[31mVocê já passou do prazo de se alistar no serviço militar a {idade - 18} ano(s); em '
          f'{date.today().year - (idade - 18)}')
