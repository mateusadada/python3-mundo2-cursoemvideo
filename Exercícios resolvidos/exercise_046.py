# Faça um programa que mostre uma contagem regressiva na tela para o estouro de fogos de artifício, indo de 10 até 0,
# com uma pausa de 1 segundo entre eles.

from time import sleep

print('Bem-vindo ao programa de contagem regressiva de fogos de artifício!'
      '\n\n\033[32m*** CONTAGEM REGRESSIVA ***\n\033[33m')

for i in range(10, -1, -1):
    sleep(1)
    print(i)

sleep(1)
print('\n\033[31mESTOURAR OS FOGOS!!!')
