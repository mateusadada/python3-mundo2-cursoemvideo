# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, conforme
# a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

print('Bem-vindo ao programa de cálculo da média!')

nota1 = float(input('1º nota: '))
nota2 = float(input('2º nota: '))

media = (nota1 + nota2) / 2

if media >= 7:
    print(f'\n\033[32mAPROVADO!\033[m Média {media:.1f}')
elif media < 5:
    print(f'\n\033[31mREPROVADO!\033[m Média {media:.1f}')
else:
    print(f'\n\033[33mRECUPERAÇÃO!\033[m Média {media:.1f}')
