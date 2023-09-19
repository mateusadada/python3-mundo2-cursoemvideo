print('Bem-vindo ao programa que faz uma saudação!')

nome = str(input('Qual é o seu nome? '))

if nome == 'Mateus':
    print('\nQue nome bonito!')
elif nome == 'Julia' or nome == 'Lívia' or nome == 'Helena':
    print('\nSeu nome é bem popular no Brasil!')
else:
    print('\nSeu nome é bem normal!')

print(f'Tenho um bom dia, \033[33m{nome}\033[m!')
