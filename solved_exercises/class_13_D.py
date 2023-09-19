total = 0

# índice 0 até o 2
for i in range(3):
    numero = int(input(f'{i + 1}º número: '))
    total += numero

print(f'\n\033[33mA soma de todos os valores é {total}\033[m'
      f'\n\nEND')
