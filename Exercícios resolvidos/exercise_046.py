# Faça um programa que mostre uma contagem regressiva na tela para o estouro de fogos de artifício, indo de 10 até 0,
# com uma pausa de 1 segundo entre eles.

from time import sleep

print('Bem-vindo ao programa de contagem regressiva de fogos de artifício!'
      '\n\n\33[32m*** CONTAGEM REGRESSIVA ***\n')

for i in range(10, -1, -1):
    sleep(1)
    print('\33[33m', i)

sleep(1)
print('\n\33[31mESTOURAR OS FOGOS!!!')
