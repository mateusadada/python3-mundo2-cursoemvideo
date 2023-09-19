# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA
# MARATONA.

print('Bem-vindo ao programa de que verifica se uma frase é palíndromo!')

frase = str(input('Digite uma frase qualquer: ')).upper().replace(' ', '')
frase_invertida = ''

if len(frase) > 0:
    for i in range(len(frase) - 1, -1, -1):
        frase_invertida += frase[i]

    if frase == frase_invertida:
        print(f'\n\033[32mA frase "{frase}" é um PALÍNDROMO!')
    else:
        print(f'\n\033[33mA frase "{frase}" NÃO é um PALÍNDROMO!')

else:
    print('\n\033[31mInválido! Não foi digitado nenhum texto. Tente novamente!')
