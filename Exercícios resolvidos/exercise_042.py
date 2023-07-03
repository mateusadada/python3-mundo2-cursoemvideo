# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

print('Bem-vindo ao programa de cálculo do tipo de um triângulo!')

reta1 = float(input('1º reta: '))
reta2 = float(input('2º reta: '))
reta3 = float(input('3º reta: '))

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('\n\033[33mÉ possível formar um triângulo ', end='')

    if reta1 != reta2 != reta3 != reta1:
        print('ESCALENO')

    elif reta1 == reta2 != reta3 or reta1 == reta3 != reta2 or reta2 == reta3 != reta1:
        print('ISÓSCELES')

    else:
        print('EQUILÁTERO')

else:
    print('\n\033[31mNÃO é possível formar um triângulo!')
