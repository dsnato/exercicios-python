from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Vamos jogar?
Escolha sua opção:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
''')
jogador = int(input('Escolha uma opção: '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
sleep(0.5)
print('-=-' * 13)
print(f'O computador escolheu {itens[computador]}.')
print(f'O jogador escolheu {itens[jogador]}.')
print('-=-' * 13)
if computador == 0:
    if jogador == 0:
        print('Empatou!')
    elif jogador == 1:
        print('Jogador Venceu!')
    elif jogador == 2:
        print('Jogador Perdeu!')
    else:
        print('Jogada inválida!')
elif computador == 1:
    if jogador == 0:
        print('Jogador Perdeu!')
    elif jogador == 1:
        print('Empatou!')
    elif jogador == 2:
        print('Jogador Venceu!')
    else:
        print('Jogada inválida!')
elif computador == 2:
    if jogador == 0:
        print('Jogador Venceu!')
    elif jogador == 1:
        print('Jogador Perdeu!')
    elif jogador == 2:
        print('Empatou!')
    else:
        print('Jogada inválida!')