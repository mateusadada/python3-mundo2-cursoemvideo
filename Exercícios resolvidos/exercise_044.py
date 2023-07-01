# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
# pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

print('Bem-vindo ao programa de cálculo de um produto!')

preco_normal = float(input('Informe o preço normal: R$ '))
condicao_de_pagamento = int(input('1 - À vista dinheiro/cheque: 10% de desconto'
                                  '\n2 - À vista no cartão: 5% de desconto'
                                  '\n3 - Até 2x no cartão: preço normal'
                                  '\n4 - 3x ou mais no cartão: 20% de juros'
                                  '\nOpção: '))

if condicao_de_pagamento == 1:
    print(f'\n\033[33mValor a pagar (10% de desconto): R$ {preco_normal * 0.90:.2f}')
elif condicao_de_pagamento == 2:
    print(f'\n\033[33mValor a pagar (5% de desconto): R$ {preco_normal * 0.95:.2f}')
elif condicao_de_pagamento == 3:
    print(f'\n\033[33mValor a pagar é o preço normal: R$ {preco_normal:.2f}')
elif condicao_de_pagamento == 4:
    print(f'\n\033[33mValor a pagar (20% de juros): R$ {preco_normal * 1.2:.2f}')
else:
    print('\n\033[31mOpção inválida!')
