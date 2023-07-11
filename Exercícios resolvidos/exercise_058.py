# Melhore o jogo do DESAFIO 028 (exercise_028) onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o
# jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

print('Bem-vindo ao programa de adivinhação de um número entre 0 e 10!')

contador = 1
computador = randint(0, 10)
jogador = int(input('Digite um número [0 até 10]: '))

while 0 > jogador or jogador > 10:
    jogador = int(input('\033[31mOpção inválida! Tente novamente [0 até 10]: \033[m'))


while jogador != computador:
    jogador = int(input('\033[33mVocê errou! Tente novamente [0 até 10]: \033[m'))

    while 0 > jogador or jogador > 10:
        jogador = int(input('\033[31mOpção inválida! Tente novamente [0 até 10]: \033[m'))

    contador += 1

print(f'\n\033[32mParabéns, você acertou o número {computador} após {contador} tentativa(s) válidas')
