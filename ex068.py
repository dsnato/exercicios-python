from random import randint
v = d = c = 0
print('----- PAR ou ÍMPAR -----')
print('Vamos jogar?')
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total foi {total}.', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            d += 1
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            d += 1
    continuar = str(input('Quer jogar novamente? [S/N]: ')).upper().strip()[0]
    if continuar == 'S':
        pass
    else:
        c = v + d
        break
print(f'''Você jogou {c} vezes, venceu {v} vezes e perdeu {d}.
### Foi bom jogar com você! Volte sempre! ###''')
