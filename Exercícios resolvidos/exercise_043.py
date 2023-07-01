# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre
# seu status, conforme a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

print('Bem-vindo ao programa de cálculo de IMC!')

peso = float(input('Informe o peso (kg): '))
altura = float(input('Altura (mt): '))

imc = peso / altura ** 2

print(f'\nIMC: \033[33m{imc:.1f}\033[m'
      f'\nSituação: ', end='')

if imc < 18.5:
    print('\033[31mAbaixo do peso')
elif 18.5 <= imc < 25:
    print('\033[32mPeso ideal')
elif 25 <= imc < 30:
    print('\033[33mSobrepeso')
elif 30 <= imc < 40:
    print('\033[31mObesidade')
else:
    print('\033[31mObesidade mórbida')
