# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário
# do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o
# empréstimo será negado.

# print('Bem-vindo ao programa de aprovação de empréstimo de uma casa!')

valor_da_casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos que vai ser pago: '))

prestacao_mensal = valor_da_casa / anos

if prestacao_mensal / salario > 0.3:
    print(f'\n\033[31mEmpréstimo NEGADO!\033[m Valor da prestação mensal acima do limite '
          f'({prestacao_mensal / salario * 100:.1f}%)')
else:
    print(f'\n\033[32mEmpréstimo APROVADO!\033[m Valor da prestação mensal abaixo do limite '
          f'({prestacao_mensal / salario * 100:.1f}%)')
