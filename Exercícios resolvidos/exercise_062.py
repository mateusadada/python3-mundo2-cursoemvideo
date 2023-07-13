# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando
# ele disser que quer mostrar 0 termos.

# print('Bem-vindo ao programa de cálculo de n números de uma PA!')

print('Bem-vindo ao programa de cálculo de uma PA!')

primeiro_termo = int(input('Digite o 1º termo de uma PA: '))
razao = int(input('Razão: '))

contador_termos = 0
quantidade_termos = 1

while quantidade_termos != 0:
    contador = 0
    quantidade_termos = int(input('Mostrar quantos termos (0 p/ sair)? '))

    while contador < quantidade_termos:
        print(f'{contador_termos + 1}º termo: \033[33m{primeiro_termo + (razao * contador_termos)}\033[m')
        contador += 1
        contador_termos += 1

    print()

print('\033[33mSaindo... Até logo...')
